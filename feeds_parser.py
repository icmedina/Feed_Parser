#!/usr/bin/python3

# import news feeds from specified urls
# filter news based on keywords
# required packages: feedparser & re (regular expression)
# install feedparser: sudo pip install feedparser

import webbrowser
import feedparser
import re

#from future import Future

# pull down all feeds
# future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
# block until they are all in
# feeds = [future_obj() for future_obj in future_calls]

file_in = "feeds_url"	# file input
keywords = ['USD[/-]JPY',' Japan ', ' US '] #'EUR[/-]USD']
out = open('rss.html','w')
body = []

def process(line):
  if 'xmlUrl' in line:
    rss = re.split ('xmlUrl=\"|\"/>',line)
    f = feedparser.parse(rss[1])
    for feed in f.entries:
      for keyword in keywords:
        WordFound = re.search(keyword, feed.title,  re.I) #re.I - case insensitive
        if WordFound:
          filtered_rss =(feed.title+ "\t" +feed.published+ "\n" +feed.description+ "\n" +feed.link+ "\n")
          body.append(filtered_rss)
          print (filtered_rss)


with open(file_in) as f:
  for line in f:
    process(line)

print (body)

html_body = ', '.join(body)
header = "<html><head></head><body><p>"
footer = "</p></body></html>"

message = header + html_body + footer
out.write(message)
out.close()

webbrowser.open_new_tab('rss.html')
