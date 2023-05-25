from classes.plane import AirbusA220
from classes.flight import Flight
from classes.passenger import Passenger

# from classes.passenger import Passenger


def main():
    # Declare passengers
    passenger_one = Passenger("Baghera")
    passenger_two = Passenger("Jones")
    # Declare plane
    airbusA220 = AirbusA220("F-WWBQ")
    # Declare flight with previous plane declared
    flight = Flight("AF123", airbusA220)

    # Assign seat for passengers
    flight.assign_seat([passenger_one, passenger_two])
    flight.show_reservation_details([passenger_one, passenger_two])

    print(flight.get_avalaible_seats())

    # Reassign seat to passenger one
    flight.assign_seat([passenger_one, passenger_two])

    print("")
    print("")

    print(flight.get_avalaible_seats())
    flight.show_reservation_details([passenger_one, passenger_two])


if __name__ == "__main__":
    main()
