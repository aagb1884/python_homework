class Rooms:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guestlist = []
        self.songlist = []
    
    def add_guest_to_room(self, name):
        if len(self.guestlist) < self.capacity:
            self.guestlist.append(name)
        elif len(self.guestlist) > self.capacity:
            self.guestlist.remove(name)

    def remove_guest_from_room(self, name):
        # if guest in guest.list:
        self.guestlist.remove(name)

    def add_song_to_room(self, song):
        self.songlist.append(song)

# - What happens if there are more guests trying to be checked in than
# there is free space in the room?
# <!-- once capacity is over -->
# test > code to stop access once capacity reached - conditional
# if len guestlist == capacity then break funct.

# free_spaces function to check if there is capacity