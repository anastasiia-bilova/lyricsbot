"""
Custom implementation of Telegram Bot.
"""
import telebot
from telebot import types
from telebot.apihelper import ApiException

from config import TOKEN
from conn_to_db import (
    create_song_data_table,
    create_user_state_table,
    get_author_song,
    get_title_song,
    get_user_state,
    insert_chat_id_to_user_state,
    insert_song_data_to_song_data_table,
    update_author_song,
    update_title_song,
    update_user_state,
)
from domains.genius.genius import get_song_text


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def msg(message):
    """
    Docs.
    """
    create_user_state_table()
    insert_chat_id_to_user_state(message.chat.id)

    create_song_data_table()
    insert_song_data_to_song_data_table(message.chat.id)

    render_initial_keyboard(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Docs.
    """
    if call.data == "author":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Write the author song!")

        update_user_state(call.message.chat.id, 1)


@bot.message_handler(func=lambda message: True)
def handle_request_text(message):
    """
    Docs.
    """
    if get_user_state(message.chat.id) == 1:
        get_user_state(message.chat.id)
        bot.send_message(message.chat.id, "Write the song name!")

        update_user_state(message.chat.id, 2)

        author_song = message.text
        update_author_song(author_song, message.chat.id)

    else:
        title_song = message.text
        update_title_song(title_song, message.chat.id)

        bot.send_message(message.chat.id, "Wait a few seconds, please.")

        author = get_author_song(message.chat.id)
        title = get_title_song(message.chat.id)
        update_user_state(message.chat.id, 0)

        try:
            bot.send_message(message.chat.id, get_song_text(author, title))
        except ApiException:
            bot.send_message(message.chat.id, "The song is not available, sorry.")

        render_initial_keyboard(message)


def render_initial_keyboard(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton("Press me!",
                                            callback_data="author"))
    bot.send_message(message.chat.id,
                     "If you wanna receive lyrics, press the button and follow the instructions:",
                     reply_markup=keyboard)

if __name__ == '__main__':
    print('Telegram bot called @LyricsBot is running on the address t.me/SearchMyLyricsBot')
    bot.polling(none_stop=True)
