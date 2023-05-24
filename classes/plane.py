from abc import ABC


class Plane(ABC):
    def __init__(self, registration_number, capacity):
        self.registration_number = registration_number
        self.capacity = capacity
        self.seat_map = {}

    def initialize_seat_map(self, rows, seats_per_row):
        for row in range(1, rows + 1):
            for seat_index in range(1, seats_per_row + 1):
                seat_letter = chr(ord("A") + seat_index - 1)
                seat_number = f"{row}{seat_letter}"
                self.seat_map[seat_number] = None


class AirbusA320(Plane):
    def __init__(self, registration_number):
        row = 20
        seats_per_row = 6
        capacity = row * seats_per_row
        super().__init__(registration_number, capacity=capacity)
        self.registration_number = registration_number
        super().initialize_seat_map(row, seats_per_row)


class AirbusA220(Plane):
    def __init__(self, registration_number):
        row = 30
        seats_per_row = 6
        capacity = row * seats_per_row
        super().__init__(registration_number, capacity=capacity)
        self.registration_number = registration_number
        super().initialize_seat_map(row, seats_per_row)
