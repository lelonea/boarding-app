from src.api.dtos import BoardingCard
from src.impl.journey_service import JourneyService


class BoardingApi:

    @staticmethod
    def sort_journey(boarding_cards_data):
        """
        Accepts a list of dictionaries representing boarding cards, serializes them into BoardingCard objects,
        sorts them, and returns a sorted list of journey instructions.

        :param boarding_cards_data: List of dictionaries, each representing a boarding card.
        :return: List of strings, each representing a step in the journey.
        """
        # Serialize dictionaries into BoardingCard objects
        boarding_cards = [
            BoardingCard(**card_data) for card_data in boarding_cards_data
        ]

        # Use JourneyService to sort boarding cards and generate journey instructions
        try:
            sorted_cards = JourneyService.sort_boarding_cards(boarding_cards)
            instructions = JourneyService.generate_journey_instructions(sorted_cards)
            return instructions
        except ValueError as e:
            return [str(e)]
