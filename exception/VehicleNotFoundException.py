class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found."):
        super().__init__(message)
