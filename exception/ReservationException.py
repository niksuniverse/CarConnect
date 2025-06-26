class ReservationException(Exception):
    def __init__(self, message="Reservation error. Check availability or input."):
        super().__init__(message)
