from classes.plane import Plane, AirbusA320, AirbusA220


def test_initialize_seat_map():
    # Test case for Plane.initialize_seat_map()
    plane = Plane("ABC123", capacity=100)
    plane.initialize_seat_map()

    assert len(plane.seat_map) == 100  # Expected seat map size

    # Check if all seats are initialized as None
    for seat_number in plane.seat_map:
        assert plane.seat_map[seat_number] is None


def test_airbus_a320_initialization():
    # Test case for initializing AirbusA320
    registration_number = "XYZ789"
    plane = AirbusA320(registration_number)

    assert plane.registration_number == registration_number
    assert plane.capacity == 120  # Expected capacity for Airbus A320

    # Check if seat map is initialized correctly
    assert len(plane.seat_map) == 120  # Expected seat map size


def test_airbus_a220_initialization():
    # Test case for initializing AirbusA220
    registration_number = "PQR456"
    plane = AirbusA220(registration_number)

    assert plane.registration_number == registration_number
    assert plane.capacity == 180  # Expected capacity for Airbus A220

    # Check if seat map is initialized correctly
    assert len(plane.seat_map) == 180  # Expected seat map size
