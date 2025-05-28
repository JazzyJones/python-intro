def is_email_valid(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def rectangle_area(a, b):
    return a * b

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def convert_date(date_str):
    from datetime import datetime
    return datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y/%m/%d")

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
