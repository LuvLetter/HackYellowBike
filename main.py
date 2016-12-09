#!/usr/bin/python
"Hack yellow bike!"
import time
from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import json
import sqlite3

def main():
    try:
        db = sqlite3.connect('test.db')
        db.execute('''CREATE TABLE YBC
       (ID INT KEY    NOT NULL,
       PWD  INT   NOT NULL
       );''')
        bot_info = open('bot_info.json')
        bot_info = json.loads(bot_info.read())
        bot = TelegramBot(bot_info["id"]+':'+bot_info["token"])
        conn = sqlite3.connect('test.db')
        offsets = bot_info["offsets"]
        while True:
            updates = bot.get_updates(offsets).wait()
            for update in updates:
                print(str(update.message.sender.id)+':'+update.message.text)
                sender_id = update.message.sender.id
                content = update.message.text.split()
                offsets = update.update_id + 1
                bot_info['offsets'] = offsets
                if(content[0] == '/start'):
                    bot.send_message(sender_id, "Welcome.").wait()
                    print("SENT:" + str(sender_id) + ", update_id:" + str(offsets))
                elif(content[0] == '/query'):
                    print("query")
                    cursor = db.execute("SELECT * FROM YBC WHERE ID=?", content[1])
                    print(cursor)
                elif(content[0] == '/set'):
                    db.execute("INSERT INTO YBC (ID, PWD) \
                      VALUES (?,?)",(content[1], content[2]));
                    db.commit()
                    print("set")
                print("done")
                time.sleep(1)
    except KeyboardInterrupt:
        with open('bot_info','wt') as save:
            bot_info['offsets'] = offsets
            print(json.dumps(bot_info))
            print(json.dumps(bot_info), file = save)
        db.close()
        exit()
    except Exception:
        db.close()

# def getPWD(content):
#
#
# def setPWD(conten):





if __name__ == '__main__':
    main()
