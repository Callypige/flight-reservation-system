from classes.plane import AirbusA220

# from classes.passenger import Passenger


def main():
    airbusA220 = AirbusA220("F-WWBQ")
    print(f"A plane is available : {airbusA220.registration_number}")
    print(airbusA220.seat_map)


if __name__ == "__main__":
    main()
