from classes.flight import Flight
from classes.plane import AirbusA320
from classes.passenger import Passenger


def test_flight_reservation():
    # Create an AirbusA320 plane
    plane = AirbusA320("ABC123")

    # Create a flight with the plane
    flight = Flight("F123", plane)

    # Create passengers
    passenger1 = Passenger("Antoine Croute")
    passenger2 = Passenger("Daniel Croute")

    # Verify that no seat is initially assigned to the passengers
    assert passenger1.seat is None
    assert passenger2.seat is None

    # Reserve seats for the passengers
    passengers = [passenger1, passenger2]
    assert flight.assign_seat(passengers) is True

    # Verify that seats have been assigned correctly
    assert passenger1.seat is not None
    assert passenger2.seat is not None
    assert passenger1.seat != passenger2.seat

    # Verify that the assigned seats are present in the plane's seat map
    assert passenger1.seat in plane.seat_map
    assert passenger2.seat in plane.seat_map
    assert plane.seat_map[passenger1.seat] == passenger1
    assert plane.seat_map[passenger2.seat] == passenger2

    # Reassign seats to the passengers
    assert flight.assign_seat(passengers) is True

    # Verify that seats have been reassigned correctly
    assert passenger1.seat is not None
    assert passenger2.seat is not None
    assert passenger1.seat != passenger2.seat

    # Verify that the reassigned seats are present in the plane's seat map
    assert passenger1.seat in plane.seat_map
    assert passenger2.seat in plane.seat_map
    assert plane.seat_map[passenger1.seat] == passenger1
    assert plane.seat_map[passenger2.seat] == passenger2
