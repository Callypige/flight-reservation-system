from classes.plane import AirbusA320

# from classes.passenger import Passenger


def main():
    airbusA220 = AirbusA320("F-WWBQ")
    print(
        f"A plane is available : {airbusA220.registration_number}"
    )


if __name__ == "__main__":
    main()
