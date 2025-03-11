def calculate_discount(customer_type, total_purchase, membership_years):
    """Determines the discount based on customer type, purchase amount, and membership duration."""
    discount = 0
    
    if customer_type == "premium":
        if total_purchase >= 500:
            discount = 20 if membership_years >= 5 else 15
        elif total_purchase >= 200:
            discount = 12 if membership_years >= 3 else 10
        else:
            discount = 5
    elif customer_type == "regular":
        if total_purchase >= 500:
            discount = 12 if membership_years >= 3 else 10
        elif total_purchase >= 200:
            discount = 8 if membership_years >= 2 else 5
        else:
            discount = 2
    else:
        discount = 0  # No discount for new or unregistered customers
    
    return discount

# Test cases with different customer profiles
customers = [
    {"customer_type": "premium", "total_purchase": 600, "membership_years": 6},
    {"customer_type": "premium", "total_purchase": 300, "membership_years": 2},
    {"customer_type": "regular", "total_purchase": 550, "membership_years": 4},
    {"customer_type": "regular", "total_purchase": 150, "membership_years": 1},
    {"customer_type": "new", "total_purchase": 400, "membership_years": 0},
]

# Apply discount logic to each customer
for customer in customers:
    discount = calculate_discount(customer['customer_type'], customer['total_purchase'], customer['membership_years'])
    print(f"Customer Type: {customer['customer_type'].capitalize()}, Purchase: ${customer['total_purchase']}, Membership: {customer['membership_years']} years -> Discount: {discount}%")