import json

from src.api.boarding_api import BoardingApi


def load_boarding_cards_from_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    file_path = "boarding_cards_example.json"
    boarding_cards_data = load_boarding_cards_from_json(file_path)

    # Sort the journey and get instructions using the BoardingApi
    journey_instructions = BoardingApi.sort_journey(boarding_cards_data)

    # Print the sorted journey instructions
    print("\n".join(journey_instructions))


if __name__ == "__main__":
    main()
