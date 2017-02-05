# jojo
A friendly Pelican theme

![snapshot](snapshots/jojo-snapshot-1.PNG)

## quick start

If you want to try jojo without your own pelican project:

```bash
$ pip install pelican markdown
$ git clone https://github.com/dokelung/jojo.git
$ cd jojo/examples
jojo/examples $ git clone https://github.com/getpelican/pelican-plugins.git
$ cd pelican-plugins
jojo/examples/pelican-plugins $ git clone https://github.com/burakkose/just_table.git
$ cd ..
# edit exconf.py
jojo/examples $ pelican content -o output -s exconf.py
jojo/examples $ cd output
jojo/examples/output $ python -m pelican.server
# open your browser and goto your SITEURL, that's all!
```

If you already have your pelican project like that:

```
project
    |--content
    |     |--...
    |
    |--themes
    |     |--...
    |
    |--pelicanconf.py
    |
    |...
```

```bash
$ cd themes
themes $ git clone https://github.com/dokelung/jojo.git
themes $ cd ..
# install needed pelican plugins
# edit pelicanconf.py
# generate pelican site by the way you are familiar with
# start the test server or publish site
# open your browser and goto SITEURL to see it!
```

## requirements

Followings are my dev environments:

* python: 3.6.0
* pip: 9.0.1
* pelican: 3.7.1
* beautifulsoup4: 4.5.3
* uikit2

Require pelican plugins:

* tipue_search: need beautifulsoup4
* just_table
* representative_image: need beautifulsoup4

## pelican settings

### basic pelican settings

See example:

```python
AUTHOR = 'jojo'
SITENAME = 'jojo'
SITEURL = 'http://localhost:8000'
DEFAULT_PAGINATION = 10
```

### templates

To fully enable all features of jojo, please specify `DIRECT_TEMPLATES` as followings:

```python
DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')
```

### paths

Actually, you don't have to fully follow the settings below, but I recommand you to follow them:

```python
# content path
PATH = 'content'

# specify plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'just_table', "representative_image"]

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

# static
STATIC_PATHS = ['images', 'articles']

# articles
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'category/{category}/{slug}/'
ARTICLE_SAVE_AS = 'category/{category}/{slug}/index.html'

# pages
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

THEME = 'path/to/jojo' # specify your own path to jojo
```

### core settings of jojo

put all photos under content/images and just specify the base name of it in following settings:

#### specify site icon

```python
SHORTCUT_ICON = 'jojo.jpg'
```

#### settings of right side panels

##### author panel

`AUTHOR_INFO` is used to set author panel.
`SOCIAL` is a variable used in `AUTHOR` to specify your social network:

```python
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
```

* `style`: modify it to adjust the appearence of social icons
* `icons`: specify the social icons you want with format `(ICON_NAME, URL)`

```python
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
    'url': os.path.join(SITEURL, 'pages', 'about-me'),
    'social': SOCIAL,
}
```

* `id`: is usually equal to `AUTHOR`
* `photo`: photo of author (placed this image under content/images)
* `intro_keywords`: tuple of tuples, each item represents a hyper link specified by format `(TEXT, URL)`
* `intro`: list of strings
* `url`: the url of about-me page
* `social`: dictionary used to specify social networks

##### newest articles

specify `NEWEST_ARTICLES` to enable related panel:

```python
NEWEST_ARTICLES = 10  # set 0 to hide this panel
```

##### user specified simple panels

```python
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
        'photo': 'food.jpg',
        'content': 'I really love it!',
        'link': ('Where to eat it?', '#'),
    },
)
```

##### related links panel

```python
RELATED_LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('mg', 'https://github.com/lucachr/pelican-mg'),
)
```

#### settings of left side buttons

set `True` to enable buttons or `False` to hide them:

```python
SHARE_BUTTONS = True
CONTROL_BUTTONS = True
```

#### settings of top elements

```python
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
                {'link':('python', os.path.join(SITEURL, 'category', 'python.html')) },
                {'type':'divider'},
                {'link':('misc', os.path.join(SITEURL, 'category', 'misc.html'))},
            )
        },
        {
            'primary': ('Archives', os.path.join(SITEURL, 'archives.html')),
        },
    ),
    'tipue_search': True,
}
```

```python
LOCATION = True
```

#### settings of footer

```python
FOOTER = {
    'year': 2017,
    'author': AUTHOR,
    'license': {
        'name': 'The MIT License',
        'link': 'https://opensource.org/licenses/MIT',
    }
}
```

#### comment system

```python
# DISQUS_SITENAME = "your disqus shortname"
# DISQUS_CONFIG = True
```
