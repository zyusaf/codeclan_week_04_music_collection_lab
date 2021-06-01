import unittest

from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Purple Rain", "Funk", "Prince")

    def test_if_album_has_title(self):
        self.assertEqual("Purple Rain", self.album.title)

    def test_if_album_has_genre(self):
        self.assertEqual("Funk", self.album.genre)

    def test_if_album_has_name(self):
        self.assertEqual("Prince", self.album.name)