class Passenger:
    def __init__(self, name, seat=None):
        self.name = name
        self.seat = seat

    def __str__(self) -> str:
        return self.name
