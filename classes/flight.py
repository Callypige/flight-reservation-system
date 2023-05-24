import textwrap


class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number
        self.plane = plane
        self.passengers = []

    def assign_seat(self, passenger):
        """
        Assigns a seat to a passenger on the flight.

        Args:
            passenger (Passenger): The passenger object for seat assignment.

        Returns:
            bool: True if the seat was successfully assigned, False otherwise.
        """
        available_seats = self.get_avalaible_seats()
        if available_seats:
            seat = available_seats[0]
            self.plane.seat_map[seat] = passenger
            passenger.seat = seat
            return True
        else:
            return False

    def get_avalaible_seats(self):
        """
        Retrieves the available seats on the plane.

        Returns:
            list: A list of seat numbers that are currently available.
        """
        available_seats = []
        for seat, passenger in self.plane.seat_map.items():
            if passenger is None:
                available_seats.append(seat)
        return available_seats

    def show_reservation_details(self, passengers=None):
        # TODO: Don't forget passengers, this function is not finished yet
        details = textwrap.dedent(
            f"""
        The flight number is {self.flight_number}
        and the plane is {self.plane}.
        """
        )
        print(details)
