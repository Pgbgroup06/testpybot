import time
import json
import telebot



BOT_TOKEN = "5399300382:AAFTPLtLwPK8yfZynK_7ZG-S-SlHXAvKPj4"

OWNER_ID = 1629550450 #write owner's user id here.. get it from @MissRose_Bot by /id


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    if msg == '/start':
        user = str(user)
        
        bot.send_message(user, "Hi")
    if msg == '/info':
        user = str(user)
          bot.send_message(user, "Made By Pgbgroup")
            
   if __name__ == '__main__':
    bot.polling(none_stop=True)
         
 
        
       
  
