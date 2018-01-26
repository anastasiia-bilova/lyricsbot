# lyricsbot

Lyricsbot is a Telegram bot, that allow user to get text of song.

![Python3](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python3](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

# Getting started

Install requirements on your environment:

```
pip3 install -r requirements.txt
```

Also good to install develop requirements and check your code with linters:

```
pip install -r requrements-dev.txt
```

Running all tests in `lyricsbot` directory to check code coverege

```
python -m unittest discover
```

And running all linting tools together to check code quality

```
flake8 lyricsbot && pylint —rcfile=setup.cfg lyricsbot && pycodestyle lyricsbot
```
