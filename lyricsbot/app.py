"""
Custom implementation of Telegram Bot.
"""
import os

import telebot
from telebot import types
from telebot.apihelper import ApiException
from flask import Flask, request

try:
    from config import TOKEN  # pylint: disable=relative-import
    from database_configurations import (  # pylint: disable=relative-import
        create_song_data_table,
        create_user_state_table,
        get_author_song,
        get_title_song,
        get_user_state,
        insert_chat_id_to_user_state,
        insert_data_to_sd_table,
        update_author_song,
        update_title_song,
        update_user_state,
    )
    from domains.genius.genius import get_song_text_from_genius  # pylint: disable=relative-import
# pylint:disable=bare-except
except:  # noqa: E722 # Python 3.5 does not contain `ModuleNotFoundError`
    from lyricsbot.config import TOKEN
    from lyricsbot.database_configurations import (
        create_song_data_table,
        create_user_state_table,
        get_author_song,
        get_title_song,
        get_user_state,
        insert_chat_id_to_user_state,
        insert_data_to_sd_table,
        update_author_song,
        update_title_song,
        update_user_state,
    )
    from lyricsbot.domains.genius.genius import get_song_text_from_genius


server = Flask(__name__)  # pylint: disable=C0103

bot = telebot.TeleBot(TOKEN)  # pylint: disable=C0103


@bot.message_handler(commands=['start'])
def msg(message):
    """
    Initial actions on the first message.
    """
    create_user_state_table()
    insert_chat_id_to_user_state(message.chat.id)

    create_song_data_table()
    insert_data_to_sd_table(message.chat.id)

    render_initial_keyboard(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Get the first message, change user state to 1.
    """
    if call.data == "author":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Write the author song!"
        )

        update_user_state(call.message.chat.id, 1)


@bot.message_handler(func=lambda message: True)
def handle_request_text(message):
    """
    Get the second message, change user state to 2.

    Return the complete user song.
    """
    if get_user_state(message.chat.id) == 1:
        get_user_state(message.chat.id)

        bot.send_message(
            message.chat.id, "Write the song name!"
        )

        update_user_state(message.chat.id, 2)

        author_song = message.text
        update_author_song(author_song, message.chat.id)

    else:
        title_song = message.text
        update_title_song(title_song, message.chat.id)

        author = get_author_song(message.chat.id)
        title = get_title_song(message.chat.id)

        update_user_state(message.chat.id, 0)

        try:
            bot.send_message(
                message.chat.id, get_song_text_from_genius(author, title)
            )
        # if the lyrics are more than 3000 characters, then it is too large for telegram message
        except ApiException:
            bot.send_message(
                message.chat.id, "The song is not available, sorry."
            )

        render_initial_keyboard(message)


def render_initial_keyboard(message):
    """
    Creates the initial inline keyboard.
    """
    keyboard = types.InlineKeyboardMarkup()

    keyboard.row(
        types.InlineKeyboardButton("Press me!", callback_data="author")
    )

    bot.send_message(
        message.chat.id,
        "If you wanna receive lyrics, press the button and follow the instructions:",
        reply_markup=keyboard
    )


@server.route("/" + TOKEN, methods=['POST'])
def getMessage():  # pylint: disable=C0103
    """
    Update for webhook.
    """
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )

    return "!", 200


@server.route("/")
def webhook():
    """
    Webhook.
    """
    bot.remove_webhook()
    bot.set_webhook(url="https://ancient-dusk-91680.herokuapp.com/" + TOKEN)

    return "!", 200


if __name__ == '__main__':

    if os.environ['ENVIRONMENT'] == 'local':
        bot.polling()

    if os.environ['ENVIRONMENT'] == 'production':
        server.run(
            host="0.0.0.0",
            port=int(os.environ.get('PORT', 5000))
        )
