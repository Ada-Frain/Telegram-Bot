from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import TOKEN, URL
from bs4 import BeautifulSoup
import requests

# функция sms будет вызвана пользователем командой /start
def sms(bot, update):
    # print(bot.message)
    bot.message.reply_text(f'привет, {bot.message.chat.first_name}', reply_markup=keyboard())

# скидывает анекдот
def anegdot(bot, update):
    receive = requests.get('http://anekdotme.ru/random')
    page = BeautifulSoup(receive.text, "html.parser")
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    bot.message.reply_text(page)

# функция parrot повторяет сообщение пользователя
def parrot(bot, update):
    bot.message.reply_text(bot.message.text)

# отвечает на получение номера телефона
def contact(bot, update):
    bot.message.reply_text(f'Спасибо, {bot.message.chat.first_name}! Мы получили ваш номер телефона.')

# отвечает на получение геоданных
def location(bot, update):
    bot.message.reply_text(f'Спасибо, {bot.message.chat.first_name}! Мы получили ваши геоданные.')

# добавляем клавиатуру
def keyboard():
    contact_btn = KeyboardButton('Send contact', request_contact=True)
    location_btn = KeyboardButton('Send location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Start', 'Anegdot'], [contact_btn, location_btn]], resize_keyboard=True)
    return my_keyboard

# функция main соединяет бота с платформой Телеграм
def main():
    my_bot = Updater(TOKEN, URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Start'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Anegdot'), anegdot))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, contact))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, location))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()

main()
