import textwrap


class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number
        self.plane = plane

    def showReservationDetails(self, passengers=None):
        # TODO: Don't forget passengers, this function is not finished yet
        details = textwrap.dedent(
            f"""
        The flight number is {self.flight_number}
        and the plane is {self.plane}.
        """
        )
        print(details)
