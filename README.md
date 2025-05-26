# rssbot
Get notified if your favourite RSS channels publish new topic.

I wanted to buy a used SteamDeck on a second-hand hardvare marketplace, and I wanted to get notified about the new deals automatically.
This insipered me to put this little script together:

RSS Feed parser for your Telegram bot.


## Requirements
1) A Telegram bot TOKEN and a chat id, HOWTO: [https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a]
   
2) Feedparser and some basic python packages, take a look into the rssbot.py includes.

## Usage
Fill the config section of the script with your telegram bot token and the chate id to whom you would like to send the messages, add rss feed urls, and at least one keyword.
If you don't want to filter the topics, then choose your keyword wisely ;)

Finnaly, schedule the script to run periodically, and your telegram bot will send you the new topics. :)

## TODO
Assign keywords to feeds.

If you find this tool useful, feel free to buy me a coffee: [https://buymeacoffee.com/elektr0ninja]
