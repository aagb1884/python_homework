import unittest
from src.guests import *
from src.karaoke_venue import *
from src.rooms import *

class TestGuests(unittest.TestCase):
    def setUp(self):
     self.guest_1 = Guests("Lewis", 10, "Toungescraper I & II")
     self.room_1 = Rooms("Mellow Vibes", 4)

     def test_guest_name(self):
         self.assertEqual("Lewis", self.guest_1.name)

    def test_guest_wallet(self):
         self.assertEqual(10, self.guest_1.wallet)

    def test_guest_pay_entry(self):
        self.venue = Venue("Sing Hole", "Mellow Vibes", 
                           100, 3)
        self.assertEqual(10, self.guest_1.wallet)
        self.assertEqual(3, self.venue.entry_fee)
        self.guest_1.pay_entry(self.venue.entry_fee)
        self.assertEqual(7, self.guest_1.wallet)
        
    def test_fave_song(self):
        self.assertEqual("Toungescraper I & II", self.guest_1.fave_song)

    