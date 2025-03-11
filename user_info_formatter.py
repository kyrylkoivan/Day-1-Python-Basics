import datetime

def format_user_info(user):
    """Formats and prints user details in a structured format."""
    print(f"ID: {user['id']:05d}")
    print(f"Name: {user['name'].title()}")
    print(f"Email: {user['email'].lower()}")
    print(f"Balance: ${user['balance']:,.2f}")
    print(f"Signup Date: {user['signup_date'].strftime('%B %d, %Y')}")
    print("-" * 40)

# Mock user database
users = [
    {"id": 1, "name": "alice smith", "email": "alice@example.com", "balance": 1234.56, "signup_date": datetime.date(2022, 5, 21)},
    {"id": 2, "name": "bob johnson", "email": "BOB@EMAIL.COM", "balance": 9876.43, "signup_date": datetime.date(2023, 7, 15)},
    {"id": 3, "name": "charlie brown", "email": "charlie@service.net", "balance": 250.75, "signup_date": datetime.date(2021, 12, 1)},
]

# Format and display each user’s details
for user in users:
    format_user_info(user)
