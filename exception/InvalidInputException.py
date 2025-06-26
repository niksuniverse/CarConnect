class InvalidInputException(Exception):
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)
