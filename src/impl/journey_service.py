class JourneyService:
    @staticmethod
    def generate_journey_instructions(sorted_cards):
        """
        Generates a list of instructions for completing a journey based on sorted boarding cards.

        Parameters:
        - sorted_cards: A list of BoardingCard objects sorted in the order of the journey.

        Returns:
        - A list of strings, where each string is an instruction for a part of the journey.
        """
        # Generate instructions for each card and add a final message indicating journey completion.
        instructions = [JourneyService.format_instruction(card) for card in sorted_cards]
        instructions.append("You have arrived at your final destination.")
        return instructions

    @staticmethod
    def format_instruction(card):
        """
        Formats a single journey instruction based on the transport type and details of a boarding card.

        Parameters:
        - card: A BoardingCard object containing details for a segment of the journey.

        Returns:
        - A string representing the formatted instruction for this segment of the journey.
        """
        # Handling instruction format based on the type of transportation.
        if card.transport_type.lower() == "bus":
            return f"Take the {card.transport_number} from {card.departure} to {card.destination}. No seat assignment."
        elif card.transport_type.lower() == "train":
            return f"Take train {card.transport_number} from {card.departure} to {card.destination}. Sit in seat {card.seat}."
        elif card.transport_type.lower() == "flight":
            return JourneyService.format_flight_instruction(card)
        else:
            return f"Take the {card.transport_type} {card.transport_number} from {card.departure} to {card.destination}."

    @staticmethod
    def format_flight_instruction(card):
        """
        Specifically formats a journey instruction for flight-type boarding cards, handling additional details.

        Parameters:
        - card: A BoardingCard object for a flight, containing departure, destination, and other details.

        Returns:
        - A string representing the detailed instruction for this flight segment of the journey.
        """
        # Construct the base instruction for the flight.
        instruction = f"From {card.departure}, take flight {card.transport_number} to {card.destination}."

        # Aggregate additional details like gate, seat, and baggage information.
        additional_details = []
        if gate := card.additional_info.get('Gate'):
            additional_details.append(f"Gate {gate},")
        if card.seat and card.seat.lower() != "no seat":
            additional_details.append(f"seat {card.seat}.")
        if baggage_drop := card.additional_info.get('Baggage drop'):
            additional_details.append(f"Baggage drop at {baggage_drop}.")
        elif baggage := card.additional_info.get('Baggage'):
            additional_details.append(f"Baggage {baggage}.")

        # Combine all parts into the final instruction.
        if additional_details:
            instruction += " " + " ".join(additional_details)

        return instruction

    @staticmethod
    def sort_boarding_cards(cards):
        """
        Sorts boarding cards to find the correct order of travel from start to destination.

        Parameters:
        - cards: A list of BoardingCard objects representing segments of a journey.

        Returns:
        - A list of BoardingCard objects sorted in the order they should be used to complete the journey.
        """
        # Create maps for departure and destination to find the starting point.
        departure_map = {card.departure: card for card in cards}
        destination_set = {card.destination for card in cards}

        # The start of the journey is a departure that isn't anyone's destination.
        start = (set(departure_map.keys()) - destination_set).pop()
        sorted_cards = []

        # Follow the chain of travel to sort the cards.
        while start in departure_map:
            card = departure_map.pop(start)
            sorted_cards.append(card)
            start = card.destination

        return sorted_cards
