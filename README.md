# lyricsbot

Lyricsbot will find the text of your favorite song!

[![Release](https://img.shields.io/github/release/anastasia-bilova/lyricsbot.svg)](https://github.com/anastasia-bilova/lyricsbot/releases)
![Build](https://travis-ci.org/anastasia-bilova/lyricsbot.svg?branch=develop)
![Codecov](https://img.shields.io/codecov/c/github/anastasia-bilova/lyricsbot/develop.svg)

![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

![bot](https://habrastorage.org/webt/jv/1v/rt/jv1vrtj7xijzcmu2n5z-mahbw6y.gif)

# Getting started

## What is LyricsBot

Lyricsbot is a Telegram bot that allows the user to receive lyrics.

Touch [@GetSongsLyricsBot](https://telegram.me/getsongslyricsbot).
Note: The song must be written in English.

All tokens and URLs are private because they are not available to users.

## Install

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

To get started you need to sign up on [ElephantSQL](https://www.elephantsql.com/).

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

Environment variables are variables that are defined for the current shell and are inherited by any child shells or processes, they are used to pass information into processes that are spawned from the shell.
It can be said that environment variables help to create and shape the environment of where a program runs.

We must use environment variable for simultaneous use of bot functions for local and production servers without changing the code.

Create the Telegram test bot with which you will work locally.

Temporarily set the environment variable `local` for the current shell and all its subprocesses:

```
export ENVIRONMENT="local"
```
To see a list of all of our environment variables and make sure that there is an environment variable, check its value:

```
env or printenv
printenv ENVIRONMENT
```

For the main bot on the Heroku server, set the environment variable `production`:

```
heroku config:set ENVIRONMENT=production
```

This environment variable is persistent – it will remain in place across deploys and app restarts – so unless you need to change value, you only need to set it once.

Make sure that there is an environment variable, check its value:

```
heroku config or heroku config:get ENVIRONMENT
```

Access the environment variables using the `os.environ['ENVIRONMENT']` template in Python.

For instance:

```
if os.environ['ENVIRONMENT'] == 'production':
    SERVER.run(
        host="0.0.0.0",
        port=int(os.environ.get('PORT', 5000))
    )

if os.environ['ENVIRONMENT'] == 'local':
    bot.polling()
```

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