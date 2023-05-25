import textwrap
from typing import List
from classes.passenger import Passenger


class Flight:
    def __init__(self, number, plane):
        self.number = number
        self.plane = plane
        self.passengers = []

    def assign_seat(self, passengers: List[Passenger]):
        """
        Assigns a seat to a passenger on the flight.

        Args:
            passengers (List[Passenger]): A list of Passenger objects.

        Returns:
            bool: True if the seat was successfully assigned, False otherwise.
        """
        for passenger in passengers:
            available_seats = self.get_avalaible_seats()
            if available_seats:
                if passenger.seat:
                    # if passenger has already a seat
                    # then free the old seat
                    # and reattriute the new one
                    self.plane.seat_map[passenger.seat] = None
                seat = available_seats[0]
                self.plane.seat_map[seat] = passenger
                passenger.seat = seat
            else:
                return False
        return True

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
        if not available_seats:
            return False
        return available_seats

    def show_reservation_details(self, passengers: List[Passenger]):
        """
        Displays the reservation details for one or more passengers.
        Args:
            passengers (List[Passenger]): A list of Passenger objects.
        """
        for passenger in passengers:
            if passenger.seat:
                details = textwrap.dedent(
                    f"""
                    Reservation details :
                    The flight number is {self.number}
                    and the plane is {self.plane.registration_number}.
                    The passenger is {passenger.name}
                    Their seat is {passenger.seat}
                    """
                )
                print(details)
            else:
                print(f"{passenger.name} has not seat")
