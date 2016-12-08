"Hack yellow bike!"
import time
from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import sqlite3
import json

def main():
    with open('bot_info.json') as bot_info:
        bot = TelegramBot(json.load(bot_info))
    updates = bot.get_updates().wait()
    user_id = int(-139223745)
    mints = -1
    while True:
        print(u'{} {}'.format(message.time, message.text))
        bot.send_message(user_id, "start").wait()
        time.sleep(10)

# def getShoolID():
#
# def getBikeID():
#
# def getPWD():
#
# def addPWD():

if __name__ == '__main__':
    main()
