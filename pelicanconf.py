#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = [u'matthew', u'matt', u'allison', u'katherine']
SITENAME = u'so many fires'
SITEURL = 'https://somanyfires.github.io/'
#SITEURL = 'http://localhost:8000'

THEME = "pelican-themes/graymill"
#LOAD_CONTENT_CACHE = False
DISPLAY_SUMMARY = True
IMAGE_HEADER = True # place "header.png" in <project>/theme/images/
IMAGE_EMBLEM = True # place "emblem.png" in <project>/theme/images/

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('WAMPASTOMPA store', 'https://www.zazzle.com/wampastompa/products'),
         )

# Social widget
SOCIAL = (('WAMPASTOMPA', 'https://twitter.com/_wampa__stompa'),
          )

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
PAGES = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
