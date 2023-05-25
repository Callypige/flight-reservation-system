from classes.passenger import Passenger


def test_passenger_init():
    # Test case: Initialize Passenger object with name only
    passenger = Passenger("Antoine Croute")
    assert passenger.name == "Antoine Croute"
    assert passenger.seat is None

    # Test case: Initialize Passenger object with name and seat
    passenger = Passenger("Daniel Croute", "A1")
    assert passenger.name == "Daniel Croute"
    assert passenger.seat == "A1"


def test_passenger_str():
    # Test case: Verify __str__() method
    passenger = Passenger("Antoine Croute")
    assert str(passenger) == "Antoine Croute"

    passenger = Passenger("Daniel Croute", "A1")
    assert str(passenger) == "Daniel Croute"
