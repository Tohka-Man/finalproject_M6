from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from logic import *
import threading
import time
from config import *
import tempfile

bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Добро пожаловать в бот, я помогу тебе сделать заказ в нашем магазине
    Используй команду /help чтобы изучить доступные комады бота""")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Вот доступные команды на данный момент:
    /availability - показывает наличие в магазине вместе с ценами
    /products - показывает что ты можешь приобрести в магазине под заказ и за какую стоимость
    (Бот не окончен до конца, ожидайте новые команды)""")


bot.infinity_polling()