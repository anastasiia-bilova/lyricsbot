# lyricsbot

Lyricsbot is a Telegram bot, that allow user to get text of song.

![Build](https://travis-ci.org/anastasia-bilova/lyricsbot.svg?branch=develop)
![Codecov](https://img.shields.io/codecov/c/github/anastasia-bilova/lyricsbot/coverage.svg)
![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

![startpage](https://habrastorage.org/webt/xz/ry/ev/xzryevmf9ntv_9ob0egmk5xag1q.png)
![button](https://habrastorage.org/webt/vk/s4/lx/vks4lx6y2mgk_qmmo_k55wg95-w.png)
![title](https://habrastorage.org/webt/at/ck/gv/atckgvcgej_dscqf2u0nwr_qoka.png)
![lyrics](https://habrastorage.org/webt/8e/xu/ra/8exuraxxk0rjj84foj98y4xhfwg.png)

# Getting started

Install requirements on your environment:

```
pip3 install -r requirements.txt
```

## Deploy to Heroku

Create your [Heroku account](https://signup.heroku.com/?c=70130000001x9jFAAQ), install the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and install [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03), if you still have not done this.

Clone the application from Git to your working directory:

```
git clone https://github.com/anastasia-bilova/lyricsbot.git
```

Log in on Heroku CLI to allow both the `heroku` and `git` commands to operate: 

```
heroku login
```

Create your own application on Heroku in your working directory:

```
heroku create
```

Deploy your application:

```
git push heroku heroku:master
```

Ensure that at least one instance of the app is running:

```
heroku ps:scale web=1
```

View information about your running app:

```
heroku logs --tail
```

Check that everything is working:

```
heroku open
```

To restart a server on Heroku:

```
heroku restart or heroku restart -a app_name
```

## Database

Use the ElephantSQL is a PostgreSQL database hosting service. 
Will manage administrative tasks of PostgreSQL, such as installation, upgrades to latest stable version and backup handling.

To get started you need to sign up on [ElephantSQL](https://www.elephantsql.com/)

Create a new instance:

![newinstance](https://habrastorage.org/webt/ik/nj/b7/iknjb7cfcne0nfnip7dsiiip4vu.png)

Connection URL format: postgres://username:password@hostname/databasename

![urlformat](https://habrastorage.org/webt/fv/64/qh/fv64qh3pzgwdagpdk8tybjgt3pe.png)

Install PostgreSQL database:

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

Switch over to the postgres account on your server and access a Postgres prompt immediately:

```
sudo -i -u postgres
psql postgres://username:password@hostname/databasename
```

Or you can do this in one step:

```
sudo -u postgres psql postgres://username:password@hostname/databasename
```

## Environment variables


## Development

Good to install develop requirements and check your code with linters:

```
pip3 install -r requrements-dev.txt
```

Running all tests in `lyricsbot` directory to check code coverage:

```
python -m unittest discover
```

And running all linting tools together to check code quality:

```
flake8 lyricsbot && pylint lyricsbot && pycodestyle lyricsbot
```

Checking code coverage percentage and reporting:

```
coverage run --source=lyricsbot -m unittest discover
coverage report -m
```