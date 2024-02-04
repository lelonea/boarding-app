class BoardingCard:
    def __init__(self, departure, destination, transport_type, transport_number, seat, additional_info=None):
        self.departure = departure
        self.destination = destination
        self.transport_type = transport_type
        self.transport_number = transport_number
        self.seat = seat
        self.additional_info = additional_info if additional_info else {}

    def __str__(self):
        info_str = ", ".join([f"{key}: {value}" for key, value in self.additional_info.items()]).strip()
        seat_info = f"Seat: {self.seat}" if (self.seat and self.seat.lower() != "no seat") else "No seat assignment"
        return f"{self.transport_type} {self.transport_number} from {self.departure} to {self.destination}. {seat_info}{('. ' + info_str) if info_str else ''}".strip()
