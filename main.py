from classes.plane import AirbusA220
from classes.flight import Flight
from classes.passenger import Passenger

# from classes.passenger import Passenger


def main():
    # Declare one passenger
    passenger_one = Passenger("Jones")
    # Declare plane
    airbusA220 = AirbusA220("F-WWBQ")
    # Declare flight with previous plane declared
    flight = Flight("AF123", airbusA220)

    # Try to assign seat for passenger
    flight.assign_seat(passenger_one)
    print(flight.get_avalaible_seats())
    print(passenger_one.seat)


if __name__ == "__main__":
    main()
