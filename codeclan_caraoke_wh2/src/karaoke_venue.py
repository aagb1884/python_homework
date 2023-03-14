class Venue:
    def __init__(self, name, rooms, till, entry_fee):
        self.name = name
        self.rooms = rooms
        self.guests = []
        self.till = till
        self.entry_fee = entry_fee

# - Check in guests to rooms/Check out guests from rooms
# - Add songs to rooms
# who would be doing that irl? venue. so create venue. Hello venue.

# to check guests into/out of room
# need guest name
# need room name
# let's have all guests, rooms and songs in venue so they can be
# checked into rooms on request       

    def check_guest_into_venue(self, name):
        self.guests.append(name)

    def remove_guest_from_venue(self, name):
        self.guests.remove(name)

    def sell_entry(self, entry_fee, guest):
            if guest.wallet >= entry_fee:
                    self.till += entry_fee
                    guest.pay_entry(entry_fee)