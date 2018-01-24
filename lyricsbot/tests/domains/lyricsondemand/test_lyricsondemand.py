"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domain.lyricsondemand import (
    format_request_data_url,
    parse_lyrics
)


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verify data song with url and parser.
    """

    @data(
        (
            'Childish Gambino',
            'Redbone',
            'https://www.lyricsondemand.com/c/childishgambinolyrics/redbonelyrics.html',
        ),
        (
            'Florence + The Machine',
            'Rabbit Heart (raise it up)',
            'https://www.lyricsondemand.com/f/florenceandthemachinelyrics/rabbitheartraiseituplyrics.html',
        ),
    )
    @unpack
    def test_format_request_data_url(self, author_song, title_song, expected_url):
        """
        Test for verify the URL format.
        Case: url with right data.
        Expected: right url with modifying data.
        """
        result = format_request_data_url(author_song, title_song)

        self.assertEqual(expected_url, result)

    @data(
        (
            'https://www.lyricsondemand.com/c/childishgambinolyrics/redbonelyrics.html',
            '''Daylight, I wake up feeling like you won't play right
I usually know but now, that shit don't feel right
It made me put away my pride
So long, you made a nigga wait for some, so long
You make it hoverboard like that, but no wrong
I'm wishing I could make this mine, oh

If you want it, yeah
You can have it, oh, oh, oh
If you need it, ooh
We can make it, oh
If you want it
You can have it

But stay woke
Niggas creepin'
They gon' find you
Gon' catch you sleepin'
Ooh, now stay woke
Niggas creepin'
Now don't you close your eyes

Too late
You wanna make it right, but now it's too late
My peanut butter chocolate cake with Kool-Aid
I'm trying not to waste my time

If you want it, oh
You can have it, you can have it
If you need it
You better believe in something
We can make it
If you want it
You can have it, aah!

But stay woke
Niggas creepin'
They gon' find you
Gon' catch you sleepin'
Put your hands up on me
Now stay woke
Niggas creepin'
Now don't you close your eyes
But stay woke, ooh
Niggas creepin'
They gon' find you
Gon' catch you sleepin'
Ooh, now stay woke
Niggas creepin'
Now don't you close your eyes

Baby get so scandalous, oh
How'd it get so scandalous?
Oh, oh
Baby you
How'd it get...
How'd it get so scandalous?
Ooh we get so scandalous
But stay woke
But stay woke''',
        ),
    )
    @unpack
    def test_parse_lyrics(self, url, expected_result):
        """
        Test for getting song lyrics.
        Case: get song lyrics.
        Expected: song lyrics.
        """
        result = parse_lyrics(url)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
