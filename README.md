# jojo
A friendly Pelican theme

## quick start

If you want to try jojo without your own pelican project:

```bash
$ pip install pelican markdown
$ git clone https://github.com/dokelung/jojo.git
$ cd jojo/examples
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
# edit pelicanconf.py
# generate pelican site by the way you are familiar with
# start the test server or publish site
# open your browser and goto SITEURL to see it!
```

## requirement
