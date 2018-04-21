"""
Config file.
"""
import os


if os.environ['ENVIRONMENT'] == 'production':
    TOKEN = '555478289:AAHkplsoeKEf0xeJvVXrTeQ9oHMQ20hTxHI'

if os.environ['ENVIRONMENT'] == 'local':
    TOKEN = '574721215:AAGq4TJpcz-6qObpOF5gWymn-jvVBrWF2dY'

URL = 'postgres://rikdrycw:O_P2Qr5FcLWHAU6aU8h3GfiKwjhDJoYE@baasu.db.elephantsql.com:5432/rikdrycw'
