"""
Configs for Telegram bot.
"""
import os


if os.environ['ENVIRONMENT'] == 'production':
    TOKEN = '549753151:AAFmziVnt2SDwGRMsCm7_l9H4eVN_4PnS98'

if os.environ['ENVIRONMENT'] == 'local':
    TOKEN = '599550606:AAFO_IzMnF3Dk3r4L-qm7EZBXll7PhhVB0k'

URL = 'postgres://rikdrycw:U6jesojhjg6zzAjw0ijlDjqcvi6LTWEb@baasu.db.elephantsql.com:5432/rikdrycw'
