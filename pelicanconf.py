#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Allen-smith'
SITENAME = u'Coder 耗子'
SITEURL = 'http://allen-smith.github.io'

PATH = 'content'

ARCHIVES_SAVE_AS = 'archives.html'
AUTHORS_SAVE_AS = 'authors.html'

DISPLAY_PAGES_ON_MENU='false'
DISPLAY_PAGES_RIGHT='True'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'
DATE_FORMAT={"zh":("zh_CN","%Y-%m-%d,%a"),}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Github', 'https://github.com/Allen-smith'),)

# Social widget
SOCIAL = (('CSDN', 'http://www.csdn.net/'),
          ('知乎', 'http://www.zhihu.com/'),)

'''		  
PLUGIN_PATHS=u"pelican-plugins"
PLUGINS = ["sitemap"]
SITEMAP = {
    "format":"xml",
    "priorities":{
        "articles":0.7,
        "indexes":0.5,
        "pages":0.3,
    },
    "changefreqs":{
        "articles":"monthly",
        "indexes":"daily",
        "pages":"monthly",
    }
}		  
'''
DEFAULT_PAGINATION = 10
DEFAULT_LANG = u'zh'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_RIGHT = True

THEME = "pelican-themes/tuxlite_zf"

FEED_RSS = u"feeds/all.rss.xml" 
CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"

DISQUS_SITENAME = u"httpallensmithgithubio"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
