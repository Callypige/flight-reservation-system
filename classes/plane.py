class Plane:
    def __init__(self, registration_number, capacity):
        self.registration_number = registration_number
        self.capacity = capacity
        self.seat_map = {}


class AirbusA320(Plane):
    def __init__(self, registration_number):
        super().__init__(registration_number, capacity=174)
        self.registration_number = registration_number


class AirbusA220(Plane):
    def __init__(self, registration_number):
        super().__init__(registration_number, capacity=148)
        self.registration_number = registration_number
