from abc import ABC


class Plane(ABC):
    def __init__(self, registration_number, capacity):
        self.registration_number = registration_number
        self.capacity = capacity
        self.seat_map = {}

    def initialize_seat_map(self):
        """
        Initializes the seat map of the plane.
        """
        seats_per_row = 1
        rows = self.capacity

        while rows * seats_per_row < self.capacity:
            seats_per_row += 1
            rows = int(self.capacity / seats_per_row)

        for row in range(1, rows + 1):
            for seat_index in range(1, seats_per_row + 1):
                seat_letter = chr(ord("A") + seat_index - 1)
                seat_number = f"{row}{seat_letter}"
                self.seat_map[seat_number] = None


class AirbusA320(Plane):
    def __init__(self, registration_number, capacity=120):
        super().__init__(registration_number, capacity=capacity)
        self.registration_number = registration_number
        super().initialize_seat_map()


class AirbusA220(Plane):
    def __init__(self, registration_number, capacity=180):
        capacity = 180
        super().__init__(registration_number, capacity=capacity)
        self.registration_number = registration_number
        super().initialize_seat_map()
