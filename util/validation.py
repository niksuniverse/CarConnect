import re

def is_valid_name(name):
    return bool(re.fullmatch(r"[A-Za-z]{2,50}", name.strip()))

def is_valid_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email.strip()))

def is_valid_phone(phone):
    return bool(re.fullmatch(r"\d{10}", phone.strip()))

def is_valid_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{5,20}", username.strip()))

def is_valid_password(password):
    return len(password.strip()) >= 6  # Add stronger checks if needed
