class Passenger:
    def __init__(self, name, seat=None):
        """
        Initializes a Passenger object.

        Args:
            name (str): The name of the passenger.
            seat (str, optional): The assigned seat of the passenger.
            Defaults to None.
        """
        self.name = name
        self.seat = seat

    def __str__(self) -> str:
        """
        Returns the string representation of the passenger.

        Returns:
            str: The name of the passenger.
        """
        return self.name
