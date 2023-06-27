class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.s_capacity = None

    def seat_capacity(self, s_capacity):
        self.s_capacity = s_capacity

    def display_properties(self):
        print("Vehicle Properties:")
        print("Color: ", self.color)
        print("Maximum Speed: ", self.max_speed)
        print("Mileage: ", self.mileage)
        print("Seating Capacity: ", self.s_capacity)

# Creating objects of the Vehicle class
car1 = Vehicle(200, 50000)
car1.seat_capacity(5)
car1.display_properties()

car2 = Vehicle(180, 75000)
car2.seat_capacity(4)
car2.display_properties()