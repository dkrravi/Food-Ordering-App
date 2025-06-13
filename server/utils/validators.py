import re

def is_valid_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email)

def is_strong_password(password):
    return len(password) >= 6
