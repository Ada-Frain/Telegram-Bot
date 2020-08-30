from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import TOKEN, URL
from handlers import *
from utiliti import keyboard


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

if __name__ == "__main__":
    main()
