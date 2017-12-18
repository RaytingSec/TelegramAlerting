#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram as tg
import argparse
import logging
import json


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Variables
data = {}
filepath = 'data.json'


def readdata():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def writedata():
    content = json.dumps(data, indent=4)
    with open('data.json', 'w') as f:
        f.write(content)


def start(bot, update):
    update.message.reply_text('Hello, this bot is still under devlopment')


def register(bot, update):
    chat = update.effective_chat
    username = chat.username
    if username not in data['authorized_users']:
        return
    fullname = "%s %s" % (chat.first_name, chat.last_name)
    data['fullname'] = fullname
    data['chat_id'] = chat.id
    writedata()
    update.message.reply_text('Hello %s, chat_id %d has been registered.' % (fullname, chat.id))


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('help text pending')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    updater = Updater(data['token'])

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    # get positions
    # get market data (index, watchlist, that kind of stuff)
    # draw chart?
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    logger.info('bot is up and running')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple alerting system using Telegram bot')
    parser.add_argument('--run', action='store_true', default=False, help='run bot server')
    parser.add_argument('--notify', action='store', type=str, help='Message to send to stored chat_id')
    args = parser.parse_args()

    data = readdata()
    if args.run:
        main()
    elif args.notify:
        bot = tg.Bot(data['token'])
        bot.send_message(chat_id=data['chat_id'], text=args.notify)
