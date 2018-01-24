"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domain.songlyrics import (
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
            'Kopecky',
            'Talk To Me',
            'http://www.songlyrics.com/kopecky/talk-to-me-lyrics/',
        ),
        (
            'florence + the machine',
            'Rabbit Heart (Raise It Up)',
            'http://www.songlyrics.com/florence-the-machine/rabbit-heart-raise-it-up-lyrics/',
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
            'http://www.songlyrics.com/florence-the-machine/rabbit-heart-raise-it-up-lyrics/',
            '''The looking glass, so shiny and new
How quickly the glamor fades
I start spinning slipping out of time
Was that the wrong pill to take?

Raise it up
You made a deal and now
It seems you have to offer up
But will it ever be enough?

Raise it up
Raise it up
It's not enough
Raise it up
Raise it up

Here I am, a rabbit hearted girl
Frozen in the headlights
It seems I made the final sacrifice

We raise it up
This offering
We raise it up

This is a gift, it comes with a price
Who is the lamb and who is the knife?
Midas is king and he holds me so tight
And turns me to gold in the sunlight

I look around but I can't find you
Raise it up
If only I could see your face
Raise it up

I started rushing towards the starlight
Raise it up
I wish that I could just be brave

I must become the lion hearted girl
Ready for a fight
Before I make the final sacrifice

We raise it up
This offering
We raise it up

This is a gift, it comes with a price
Who is the lamb and who is the knife?
Midas is king and he holds me so tight
And turns me to gold in the sunlight

Raise it up
Raise it up
Raise it up
Raise it up

And in the spring I shed my skin
And it blows away with the changing wind
The water has turned from blue to red
As towards the sky I offer it

This is a gift, it comes with a price
Who is the lamb and who is the knife?
And Midas is king and he holds me so tight
And turns me to gold in the sunlight

This is a gift, it comes with a price
Who is the lamb and who is the knife?
And Midas is king and he holds me so tight
And turns me to gold in the sunlight

This is a gift, it comes with a price
Who is the lamb and who is the knife?
And Midas is king and he holds me so tight
And turns me to gold in the sunlight
This is a gift''',
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
