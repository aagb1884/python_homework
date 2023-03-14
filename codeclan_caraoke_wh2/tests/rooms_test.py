import unittest
from src.rooms import *
from src.songs import Songs
from src.guests import Guests

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms("Mellow Vibes", 4)
        self.room_2 = Rooms("Power Balladsladslads", 6)
        self.room_3 = Rooms("Broken Air Conditioning", 8)
        self.room_list = [self.room_1, self.room_2, self.room_3]

        self.song_1 = Songs("Undone (The Sweater Song)", "Weezer")
        self.song_2 = Songs("Tame", "The Pixies")
        self.song_3 = Songs("Angels", "Robbie Williams")
        self.song_4 = Songs("You Oughta Know", "Alanis Morissette")
        self.song_5 = Songs("River", "Joni Mitchell")
        self.song_6 = Songs("Toungescraper I & II", "Desalvo")
        self.song_7 = Songs("Basscadet", "Autechre")

        self.guest_1 = Guests("Lewis", 10, "Toungescraper I & II")
        self.guest_2 = Guests("Claire", 10, "Basscadet")
        self.guest_3 = Guests("Keith", 10, "River")
        self.guest_4 = Guests("Jimbob", 11, "You Oughta Know")
        self.guest_5 = Guests("Divina", 12, "Song 2")
        self.guest_6 = Guests("Lindsay", 4, "Undone (The Sweater Song)") 
        self.guest_7 = Guests("Hilda", 5, "Undone (The Sweater Song)")
        self.guest_8 = Guests("Bluey's Dad", 8, "Angels",)
        self.guest_9 = Guests("Id Monster", 100, "Angels",)
        self.guest_10 = Guests("Omega", 20, "Angels",)
        self.guest_11 = Guests("Rassilon", 11, "Angels",)
        self.guest_12 = Guests("Tecteun", 4, "Angels",)
        self.everyone = [self.guest_1, self.guest_2, self.guest_3,
                         self.guest_4, self.guest_5, self.guest_6,
                         self.guest_7, self.guest_8, self.guest_9,
                         self.guest_10, self.guest_11, self.guest_12]

    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)

    def test_add_guest_to_room(self):
        self.assertEqual(0, len(self.room_2.guestlist))
        self.room_2.add_guest_to_room(self.guest_2)
        self.assertEqual(1, len(self.room_2.guestlist))

    
    def test_remove_guest_from_room(self):
        self.room_3.add_guest_to_room(self.guest_12)
        self.assertEqual(1, len(self.room_3.guestlist))
        self.room_3.remove_guest_from_room(self.guest_12)
        self.assertEqual(0, len(self.room_3.guestlist))

    # consider, in future, adding guards so can't remove guests
    # who ARE NOT THERE - ie. EMPTY room

    def test_add_song_to_room(self):
        self.assertEqual(0, len(self.room_2.songlist))
        self.room_2.add_song_to_room(self.song_5)
        self.assertEqual(1, len(self.room_2.songlist))
        
    def test_capacity_reached(self):
        self.room_1.add_guest_to_room(self.guest_12)
        self.room_1.add_guest_to_room(self.guest_11)
        self.room_1.add_guest_to_room(self.guest_10)
        self.room_1.add_guest_to_room(self.guest_9)
        self.assertEqual(4, len(self.room_1.guestlist))
        self.room_1.add_guest_to_room(self.guest_8)
        self.assertEqual(4, len(self.room_1.guestlist))

    # def test_fave_song_reaction(self):
    #     self.assertEqual("Whoo!", self.guest_1.fave_song_reaction(self.guest_1.fave_song))