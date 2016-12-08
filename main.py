"Hack yellow bike!"
import time
from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import sqlite3
import json

def main():
    with open('bot_info') as bot_info:
        #print(json.dump(bot_info))
        bot = TelegramBot(bot_info)
    user_id = int(-139223745)
    while True:
        updates = bot.get_updates().wait()
        for update in updates:
            print(update)
            # try:
            #     if(update.split() == "/get")
            #         bot.send_message(user_id, "start").wait()

        # print(u'{} {}'.format(message.time, message.text))
        # bot.send_message(user_id, "start").wait()
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
