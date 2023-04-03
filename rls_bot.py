# This Python file uses the following encoding: utf-8
from telebot import TeleBot
from web_parser import get_rls_list,get_document_by_url

bot = TeleBot('6000742215:AAHZsJ_Ot_GJWKKf06PXUDDGIcMosTC8-d8')
rls_pages = get_rls_list()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Добро пожаловать в базу знаний РЛС!")

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text in rls_pages.keys():
        html = get_document_by_url(rls_pages[message.text])
        bot.send_photo(message.from_user.id, html[0])
        bot.send_message(message.from_user.id, html[1])

bot.polling(none_stop=True, interval=0)