
class DatabaseConnectionException(Exception):
    def __init__(self, message="Unable to connect to the database."):
        self.message = message
        super().__init__(message)
