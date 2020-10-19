class Bus:
    '''this class defines how a bus looks like'''
    count = 0

    def __init__(self, driver, color,seats):
        self.driver= driver
        self.num_of_seats= seats
        self.color = color
        self.bus_count()

    def set_color(self,color):
        self.color = color

    def num_of_seats(self,seats):
        self.seats=seats

    def bus_count(self):
        self.count = self.count + 1

bus = Bus("Masande",66,"Yellow")
bus.num_of_seats = 45  #update the seats
bus.set_color('Red')  #update the bus color
print(bus)
print(bus.count)

