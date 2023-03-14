import unittest
from src.karaoke_venue import *
from src.rooms import Rooms
from src.guests import *
from src.songs import Songs

class TestVenue(unittest.TestCase):
    def setUp(self):  
        self.room_1 = Rooms("Mellow Vibes", 4)
        self.room_2 = Rooms("Power Balladsladslads", 6)
        self.room_3 = Rooms("Broken Air Conditioning", 8)    

        self.song_1 = Songs("Undone (The Sweater Song)", "Weezer")
        self.song_2 = Songs("Song 2", "Blur")
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

        self.venue = Venue("Sing Hole",
                           [self.room_1, self.room_2, self.room_3],
                           100, 3)

    def test_venue_name(self):
        self.assertEqual
        ("Sing Hole", self.venue.name)
        
    def test_room_name(self):
        self.assertEqual("Mellow Vibes", self.room_1.name)
    def test_room_capacity(self):
        self.assertEqual(4, self.room_1.capacity)   

    def test_song_name(self):
        self.assertEqual("River", self.song_5.name)    
    def test_song_artist(self): 
        self.assertEqual("Desalvo", self.song_6.artist)

    def test_guest_name(self):
        self.assertEqual("Jimbob", self.guest_4.name)

    def test_check_guest_into_venue(self):
        self.assertEqual(0, len(self.venue.guests))
        self.venue.check_guest_into_venue(self.guest_1)
        self.assertEqual(1, len(self.venue.guests))
   
    def test_remove_guest_from_venue(self):
        self.venue.check_guest_into_venue(self.guest_1)
        self.assertEqual(1, len(self.venue.guests))
        self.venue.remove_guest_from_venue(self.guest_1)
        self.assertEqual(0, len(self.venue.guests))

        # add rooms to list, references in tests above for that.
        # add guestlist to rooms.py so guests can be added/counted
        # refer back to past labs for examples of ACT
        # to check guest into room need room and guest
        # once guest added to room should be part of room so
        # just refer to room

    def test_venue_till(self):
        self.assertEqual(100, self.venue.till)

    def test_entry_fee(self):
        self.assertEqual(3, self.venue.entry_fee)

    def test_sell_entry(self):
        self.venue.sell_entry(self.venue.entry_fee, self.guest_1)
        self.assertEqual(103.00, self.venue.till)
        self.assertEqual(7.00, self.guest_1.wallet)
       