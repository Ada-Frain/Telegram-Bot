from telegram import ReplyKeyboardMarkup, KeyboardButton


# добавляем клавиатуру
def keyboard():
    contact_btn = KeyboardButton('Send contact', request_contact=True)
    location_btn = KeyboardButton('Send location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Start', 'Anegdot'], [contact_btn, location_btn]], resize_keyboard=True)
    return my_keyboard