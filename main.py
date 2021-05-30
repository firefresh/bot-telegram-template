# -*- coding: utf-8 -*-
import os
#import requests 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time as time # Librería para hacer que el programa que controla el bot no se acabe.
from time import gmtime, strftime
from utils.logger import get_logger

logger = get_logger(name='main')

def execute():
    logger.info('Start!')
    bot = telebot.TeleBot(config.get('TOKEN')) # Creamos el objeto de nuestro bot.
    apihelper.ENABLE_MIDDLEWARE = True

    @bot.middleware_handler(update_types=['message'])
    def modify_message(bot_instance, message): 
        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid > 0:
            message = str(m.chat.username) + " [" + str(cid) + "]: " + "at [" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + "]: " + m.text
        else:
            message = str(m.from_user.username) + "[" + str(cid) + "] " + "at [" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + "]: " + m.text
        logger.info(message)

    @bot.message_handler(commands=['help'])
    def command_help(m):
        cid = m.chat.id
        bot.send_chat_action(cid, 'typing')
        time.sleep(1) 
        bot.send_message( cid, COMANDOS)
        
    
    bot.polling(none_stop=True)



if __name__ == '__main__':
    execute()