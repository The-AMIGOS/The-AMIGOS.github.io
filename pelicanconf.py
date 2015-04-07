#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = u'AMIGOS Team'
SITENAME = u'AMIGOS - Australian MIcrobial GenOmics Symposium'
SITEURL = 'http://the-amigos.github.io'
RELATIVE_URLS = False
SITELOGO = 'images/AMIGOS_logo.png'

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images']

#BOOTSTRAP_FLUID = True
BOOTSTRAP_THEME = 'Paper'

PLUGINS = ['google_embed']
GMAPS_KEY = 'AIzaSyBPfFOk3PUgeWkKPcE_2oeiD7LeAS_SUHY'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Beatson Lab', 'http://beatsonlab.com/'),
         ('Darling Lab', 'http://darlinglab.org'),
         ('Holt Lab', 'https://bacpathgenomics.wordpress.com/'),
         ('Myers Lab', 'http://www.uts.edu.au/staff/garry.myers'),
         ('Petty Lab', 'http://www.uts.edu.au/staff/nicola.petty'),
         ('Seemann Lab', 'http://thegenomefactory.blogspot.com.au'),
         ('Stinear Lab', 'http://www.microbiol.unimelb.edu.au/new_research/microbiology/stinear_novo.html'),
         ('Thomas Lab', 'http://www.babs.unsw.edu.au/staff_academic/associate-professor-torsten-thomas'),
         ('Tong Lab', 'http://www.menzies.edu.au/page/Our_People/Researchers/Steven_Tong/')
        )

# Social widget

SOCIAL = (('twitter', 'http://twitter.com/WeAreTheAMIGOS'),
          ('github', 'http://github.com/The-AMIGOS'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CWD = os.getcwd()
THEME = os.path.join(CWD, "theme/pelican-bootstrap3")
SITESUBTITLE = 'Australian MIcrobial GenOmics Symposium'
FOOTER_TEXT = '(c) 2015 Mitchell Stanton-Cook'

#Tweak visually
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False

# Theme specific options for GitHub
GITHUB_USER = 'The-AMIGOS'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
