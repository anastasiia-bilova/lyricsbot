"""
Configurations of the database.
"""
import psycopg2

from lyricsbot.config import URL
from lyricsbot.errors import ConnectionError  # pylint: disable=W0622
from lyricsbot.lyricsbot_utils import parse_url_db


def connection_to_db():
    """
    Return connection to the database.
    """
    try:
        credentials = parse_url_db(URL)
        connection = psycopg2.connect(**credentials)

        return connection
    except psycopg2.OperationalError:
        raise ConnectionError('No connection!')


def create_user_state_table():
    """
    Create thr user_state table to receive the user location.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user_state "
        "(id serial PRIMARY KEY, "
        "user_id INTEGER NOT NULL, "
        "state INTEGER DEFAULT 0);"
    )

    connection.commit()


def insert_chat_id_to_user_state(mess_chat_id):
    """
    Insert the user id to user_state table.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO user_state (user_id) "
        "SELECT {0} WHERE NOT EXISTS "
        "(SELECT user_id FROM user_state "
        "WHERE user_id = {0});".format(mess_chat_id)
    )

    connection.commit()


def update_user_state(mess_chat_id, state):
    """
    Update the user_state table to track the user by his location (state).
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE user_state SET state = {0} "
        "WHERE user_id = {1};".format(state, mess_chat_id)
    )

    connection.commit()


def get_user_state(mess_chat_id):
    """
    Get the user location (state).
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT state FROM user_state "
        "WHERE user_id = {0};".format(mess_chat_id)
    )

    return cursor.fetchone()[0]


def create_song_data_table():
    """
    Create the song_data table to retain user requests.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS song_data "
        "(id serial PRIMARY KEY, "
        "user_id INTEGER NOT NULL, "
        "author_song VARCHAR DEFAULT 'empty', "
        "title_song VARCHAR DEFAULT 'empty');"
    )

    connection.commit()


def insert_data_to_sd_table(mess_chat_id):
    """
    Insert the song data to the song_data table.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO song_data (user_id) "
        "SELECT {0} WHERE NOT EXISTS "
        "(SELECT user_id FROM song_data "
        "WHERE user_id = {0});".format(mess_chat_id)
    )

    connection.commit()


def update_author_song(author_song, mess_chat_id):
    """
    Update the author_song column within the song_data table.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE song_data SET author_song = %s "
        "WHERE user_id = %s;", (author_song, mess_chat_id)
    )

    connection.commit()


def get_author_song(mess_chat_id):
    """
    Get the author of the song entered by the user.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT author_song FROM song_data "
        "WHERE user_id = {0};".format(mess_chat_id)
    )

    return cursor.fetchone()[0]


def update_title_song(title_song, mess_chat_id):
    """
    Update the title_song column within the song_data table.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE song_data SET title_song = %s "
        "WHERE user_id = %s;", (title_song, mess_chat_id)
    )

    connection.commit()


def get_title_song(mess_chat_id):
    """
    Get the title of the song entered by the user.
    """
    connection = connection_to_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT title_song FROM song_data "
        "WHERE user_id = {0};".format(mess_chat_id)
    )

    return cursor.fetchone()[0]


if __name__ == '__main__':
    connection_to_db()
