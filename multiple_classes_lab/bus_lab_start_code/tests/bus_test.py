import unittest
from src.bus import Bus
from src.bus_stop import BusStop
from src.person import Person

class TestBus(unittest.TestCase):
    def setUp(self):
        self.bus = Bus(22, "Ocean Terminal")

    
    def test_has_route_number(self):
        self.assertEqual(22, self.bus.route_number)


    
    def test_has_destination(self):
        self.assertEqual("Ocean Terminal", self.bus.destination)


   
    def test_can_drive(self):
        self.assertEqual("Brum brum", self.bus.drive())

    
    def test_starts_with_no_passengers(self):
        self.assertEqual(0, self.bus.passenger_count())

    
    def test_can_pick_up_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.assertEqual(1, self.bus.passenger_count())

   
    def test_can_drop_off_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.drop_off(person)
        self.assertEqual(0, self.bus.passenger_count())

    
    def test_can_empty_bus(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.empty_bus()
        self.assertEqual(0, self.bus.passenger_count())

    
    def test_can_pick_up_passenger_from_bus_stop(self):
        person_1 = Person("Guido van Rossum", 64)
        # creating an instance of a Person
        person_2 = Person("Carol Willing", 50)
        # creating an instance of a Person
        bus_stop = BusStop("Waverly Station")
        # crerating an instance of a Bus Stop - above lines not tested here
        bus_stop.add_to_queue(person_1)
        bus_stop.add_to_queue(person_2)
        # adding both Persons to queue
        # bus here from earlier code
        self.bus.pick_up_from_stop(bus_stop)
        # no assignment, no equals bit on left (either sign of text)
        self.assertEqual(2, self.bus.passenger_count())
# testing these two lines, rest is setup
# we know last line  something as there's a value needing to be equal
# also calling function that returns something
# bus stop could also clear its queue
        self.assertEqual(0, bus_stop.queue_length())
        # no self as bus_stop is created just above, not in self section
# self is always referrring to this class, the file it's in, the test in this instance