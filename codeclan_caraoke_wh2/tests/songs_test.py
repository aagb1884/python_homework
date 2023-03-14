import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song_2 = Songs("Song 2", "Blur")

    def test_song_name(self):
        self.assertEqual("Song 2", self.song_2.name)

    def test_song_artist(self):
        self.assertEqual("Blur", self.song_2.artist)

    if __name__ == '__main__':
        unittest.main()