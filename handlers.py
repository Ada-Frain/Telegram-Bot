from utiliti import keyboard
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
