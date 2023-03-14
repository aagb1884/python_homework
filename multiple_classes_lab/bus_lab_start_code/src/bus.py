class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []   

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger_1):
        self.passengers.append(passenger_1)

    # aim for code that makes the passenger in charge of, eg. paying
    # rather than have code where the bus - this class - manipulates their balance
    # eg passenger_to_pick_up.pay(self.fare)

    def drop_off(self, passenger_2):
        self.passengers.remove(passenger_2)


    def empty_bus(self):
        self.passengers.clear() 

    def pick_up_from_stop(self, bus_stop_1):
        for passenger in bus_stop_1.queue:
            self.pick_up(passenger)

            # or

    # def pick_up_from_stop(self, bus_stop):
    #     self.passengers.extend(bus_stop.queue)
    #     bus_stop.clear_queue()

        # extend list with another list
 
