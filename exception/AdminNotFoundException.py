class AdminNotFoundException(Exception):
    def __init__(self, message="Admin not found in the system."):
        super().__init__(message)
