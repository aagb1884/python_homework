class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []


    def pick_up(self, passenger_1):
        self.passengers.append(passenger_1)

    def add_to_queue(self, passenger_1):
        self.queue.append(passenger_1)
        
    def queue_length(self):
        return len(self.queue)
    
    def clear_queue(self):
        self.queue.clear()

    # all of these self.words and functions can be called by .name