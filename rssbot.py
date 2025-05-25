#! /usr/bin/python3

import sys
import feedparser
import socket
import subprocess
from datetime import datetime
import urllib.parse
import requests

###########################
# Config section
feeds = ("https://sample1.com/rss.xml",
        "https://sample2.com/rss.xml")
marker_file = "marker.dat"
BOT_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
chat_id = "CHAT_ID_FOR_YOUR_USER"
keywords = ("keyword1","keyword2","keyword3","keyword4")
###########################

# Load last check time from the marker file

with open(marker_file,'r') as marker:
    try:
        lastcheck = datetime.strptime(marker.read(),"%d/%m/%Y %H:%M:%S")
    except:
        lastcheck = datetime.now()

# Parse the feeds

for f in feeds:
    d = feedparser.parse(f)
    print (f"Parsing feed {f} for new entries...")
    for s in d.entries:
        pub = s.published.split(',')[1].split()
        publishedstr = f"{pub[0]} {pub[1]} {pub[2]} {pub[3]}"
        published = datetime.strptime(publishedstr,"%d %b %Y %H:%M:%S")
        if published > lastcheck:
            print(f" New item found: {s.title} {s.link}")
            interesting = False
            for kw in keywords:
                if kw in s.title.tolower():
                    interesting = True
            if interesting:
                message = urllib.parse.quote_plus(f"RSSbot: {s.title} {s.link}")
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)

# Store the current time to save last check time...

now = datetime.now()

with open(marker_file,'w') as marker:
    marker.write(now.strftime("%d/%m/%Y %H:%M:%S"))
