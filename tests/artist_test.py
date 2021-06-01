import unittest

from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Prince")

    def test_artist_has_name(self):
        self.assertEqual("Prince", self.artist.name)