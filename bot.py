import telebot

# Замените 'YOUR_TOKEN' на токен, который вы получили от BotFather
bot = telebot.TeleBot('7045412837:AAFpILlG8E4yzI2V9c9AjlgxYJDn7ZQx7Ho')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот. Напиши мне что-нибудь, и я повторю это.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()
