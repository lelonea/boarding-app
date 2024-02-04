import unittest

from src.api.boarding_api import BoardingApi


class TestJourneyService(unittest.TestCase):
    def test_sort_and_generate_instructions(self):
        boarding_cards_data = [
            {"departure": "Madrid", "destination": "Barcelona", "transport_type": "Train", "transport_number": "78A",
             "seat": "45B", "additional_info": {}},
            {"departure": "Barcelona", "destination": "Gerona Airport", "transport_type": "Bus",
             "transport_number": "airport bus", "seat": "No seat", "additional_info": {}},
            {"departure": "Gerona Airport", "destination": "Stockholm", "transport_type": "Flight",
             "transport_number": "SK455", "seat": "3A",
             "additional_info": {"Gate": "45B", "Baggage drop": "ticket counter 344"}},
            {"departure": "Stockholm", "destination": "New York JFK", "transport_type": "Flight",
             "transport_number": "SK22", "seat": "7B",
             "additional_info": {"Gate": "22", "Baggage": "will be automatically transferred from your last leg"}}
        ]
        boarding_api = BoardingApi()

        # Call the internal API to sort the journey and get instructions, passing the list of dictionaries
        journey_instructions = boarding_api.sort_journey(boarding_cards_data)

        expected_instructions = [
            "Take train 78A from Madrid to Barcelona. Sit in seat 45B.",
            "Take the airport bus from Barcelona to Gerona Airport. No seat assignment.",
            "From Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344.",
            "From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination."
        ]

        self.assertEqual(journey_instructions, expected_instructions)


if __name__ == '__main__':
    unittest.main()
