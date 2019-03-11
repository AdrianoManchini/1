@bot.message_handler(content_types=["text"])
def default_test(message):
keyboard = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="google.com")
keyboard.add(url_button)
bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик."
, reply_markup=keyboard)