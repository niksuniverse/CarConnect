class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Invalid username or password."):
        super().__init__(message)
