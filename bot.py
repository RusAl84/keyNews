
from webbrowser import get
import telebot;
from getKeyWords import getKeyWords

bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот для извлечения ключевых слов из новостей, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "интеллектуальный Бот для извлечения ключевых слов из новостей. \n Список команд: \n /k - текст для анализа \n ")
    elif splitted_text[0] == "/k":
        str1=""
        for item in splitted_text:
            if item!="/k":
                str1+=" " + item
        bot.send_message(message.from_user.id, getKeyWords(str1))    
    else:
        bot.send_message(message.from_user.id, "Привет это интеллектуальный Бот для извлечения ключевых слов из новостей, чем я могу тебе помочь? Для информации введите /help.")

bot.polling(none_stop=True, interval=0)