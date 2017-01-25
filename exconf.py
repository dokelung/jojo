#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'jojo' # theme

SITENAME = 'jojo' # theme
SITEURL = 'http://localhost:8000' # theme

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['tipue_search', 'just_table']

THEME = 'theme/jojo'

# jojo theme settings =======================================================

# put all photos in theme/static/img and just specify the base name of it in
# following settings

# site settings
DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')
SHORTCUT_ICON = 'jojo.jpg' # put this photo in theme/static/img

# right side panels
SOCIAL = {
    'style': {
        'size': 'medium', # small, medium, large
        'hover': True,    # True, False
        'button': False,  # True, False
    },
    # for SOCIAL, jojo supports uk-icon in uikit2
    # but jojo only recover following icons' color
    'icons': (
        ('envelope-square', '#'),
        ('facebook-square', '#'),
        ('github-square', '#'),
        ('google-plus-square', '#'),
        # ('linkedin-square', '#'),
        # ('skype', '#'),
        # ('twitter-square', '#'),
        # ('weixin', '#'),
    )
}
AUTHOR_INFO = {
    'id': AUTHOR,
    'photo': 'jojo.jpg',
    'intro_keywords': (
        ('a cute dog', '#'),
        ('a charming blogger', '#'),
    ),
    'intro': [
        'Hi, my name is jojo, I am a cute dog!',
        '你好，我是 jojo，一隻可愛的小狗。'
    ],
    'url': os.path.join(SITEURL, 'pages', 'about-me.html'),
    'social': SOCIAL,
}

NEWEST_ARTICALS = 10 # set 0 to hide this panel

SIMPLE_PANELS = (
    {
        'badge': {
            'string': 'Love',
            # type can be specified as '' or 'success' or 'warning' or 'danger'
            # by default, '' is blue, 'success' is green, 'warning' is orange and 'danger' is red
            # please reference to uikit2
            'type': 'danger',
        },
        'title': 'My Favorite Food',
        'photo': 'steak.jpg',
        'content': 'I really love steak!',
        'link': ('Where to eat it?', '#'),
    },
)

RELATED_LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('mg', 'https://github.com/lucachr/pelican-mg'),
)

# left side buttons
SHARE_BUTTONS = True
CONTROL_BUTTONS = True

# top
NAV = {
    'sitename': SITENAME,
    'navitems': (
        {
            'primary': ('About me', AUTHOR_INFO['url']),
        },
        {
            'primary': ('Category', os.path.join(SITEURL, 'categories.html')),
            'secondary': (
                {'type':'header', 'name':'Programming'},
                {'link':('python', os.path.join(SITEURL, 'category', 'python')) },
                {'type':'divider'},
                {'link':('misc', os.path.join(SITEURL, 'category', 'misc'))},
            )
        },
        {
            'primary': ('Archives', os.path.join(SITEURL, 'archives.html')),
        },
    ),
    'tipue_search': True,
}

LOCATION = True

# footer
FOOTER = {
    'year': 2017,
    'author': AUTHOR,
    'license': {
        'name': 'The MIT License',
        'link': 'https://opensource.org/licenses/MIT',
    }
}

# just table settings
JTABLE_TEMPLATE = """
<table class="uk-table uk-table-striped">
    {% if caption %}
    <caption> {{ caption }} </caption>
    {% endif %}
    {% if th != 0 %}
    <thead>
    <tr>
        {% if ai == 1 %}
        <th> No. </th>
        {% endif %}
        {% for head in heads %}
        <th>{{ head }}</th>
        {% endfor %}
    </tr>
    </thead>
    {% endif %}
    <tbody>
        {% for body in bodies %}
        <tr>
            {% if ai == 1 %}
            <td> {{ loop.index }} </td>
            {% endif %}
            {% for entry in body %}
            <td>{{ entry }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>
"""