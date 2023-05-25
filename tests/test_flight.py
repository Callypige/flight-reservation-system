from classes.flight import Flight
from classes.passenger import Passenger
from classes.plane import AirbusA220, AirbusA320


def test_assign_seat():
    # Test case: Assign seat to passenger
    plane = AirbusA320("F-WWBQ")
    flight = Flight("AF123", plane)

    passenger = Passenger("Antoine Croute")
    assert flight.assign_seat([passenger]) is True
    assert passenger.seat in plane.seat_map

    # Test case: Assign seat to passenger with existing seat
    passenger = Passenger("Daniel Croute", "A1")
    assert flight.assign_seat([passenger]) is True
    assert passenger.seat in plane.seat_map

    # Test case: Assign seat when no available seats
    # Create a flight with a plane that has no available seats
    plane_with_no_seats = AirbusA320("F-WERZ", capacity=0)
    flight_with_no_seats = Flight("AF456", plane_with_no_seats)

    passenger = Passenger("Antoine Daniel")
    assert flight_with_no_seats.assign_seat([passenger]) is False
    assert passenger.seat is None


def test_get_available_seats():
    # Test case: Get available seats on the plane
    plane = AirbusA320("ABC123")
    flight = Flight("F123", plane)

    available_seats = flight.get_available_seats()
    # All seats should be available initially
    assert len(available_seats) == 120

    # Assign a seat to a passenger
    passenger = Passenger("Antoine Croute")
    flight.assign_seat([passenger])

    available_seats = flight.get_available_seats()
    assert len(available_seats) == 119  # One seat should be taken


def test_show_reservation_details(capfd):
    # Test case: Show reservation details for passengers
    plane = AirbusA220("ABC123")
    flight = Flight("F123", plane)

    passenger1 = Passenger("Antoine Croute", "A1")
    passenger2 = Passenger("Daniel Croute", "B2")

    flight.show_reservation_details([passenger1, passenger2])

    captured = capfd.readouterr()
    assert "Reservation details" in captured.out
    assert passenger1.name in captured.out
    assert passenger2.name in captured.out


def test_show_reservation_details_no_seat(capfd):
    # Test case: Show reservation details for passengers without seat
    plane = AirbusA220("ABC123")
    flight = Flight("F123", plane)

    passenger = Passenger("Antoine Croute")

    flight.show_reservation_details([passenger])

    captured = capfd.readouterr()
    assert "has not seat" in captured.out
