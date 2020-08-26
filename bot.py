from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import TOKEN, URL

def sms(bot, update):
    # print(bot.message)
    bot.message.reply_text(f'привет, {bot.message.chat.first_name}')

def parrot(bot, update):
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater(TOKEN, URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()

main()
