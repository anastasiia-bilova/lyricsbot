"""
Modify url.
"""


def parse_url_db(url):  # pylint: disable=C0111

    url = url.replace('postgres://', '').replace('@', ' ').replace(':', ' ').replace('/', ' ').split()

    database_url = {}

    for part, credential in zip(range(len(url)), ['user', 'password', 'host', 'port', 'database']):
        database_url[credential] = url[part]

    return database_url
