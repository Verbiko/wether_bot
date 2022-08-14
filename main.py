#импортируем нужные библиотеки
import telebot
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot('5510222993:AAEXiMIaSC7Uoj4r2YYrot4GVoNXlTxfDYA')
#ссылка на страницу с погодой
url = 'https://sinoptik.ua/погода-минск'
#получаем текст со страницы
r = requests.get(url)
#применяем парсер
html = BS(r.content, 'html.parser')

temp = html.find_all('div', class_='main loaded')
text = html.find_all('div', class_='wDescription')

cl_temp = []
for i in temp:
    cl_temp.append(i.text)
clear_temp = ''.join(cl_temp)
print(clear_temp)

cl_text = []
for i in text:
    cl_text.append(i.text)
clear_text = ''.join(cl_text)
print(clear_text)

#описываем декоратор
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_pogoda(message):
    if message.text == 'погода' or message.text == 'Погода':
        bot.send_message(message.chat.id, 'Погода на сегодня: \n' + clear_temp + clear_text)

#зацикливаем бота, запускаем на постоянное выполнение
bot.polling(none_stop=True)


