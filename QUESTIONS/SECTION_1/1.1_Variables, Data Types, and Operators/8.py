# Build a simple bill calculator that applies a percentage discount and tax in the correct order.

def calculate_bill(p: float, discount_per: float = 10.0, tax_per: float = 15.0) -> None:
    """
    Calculates the final bill by applying discount first, then tax on the discounted amount.
    """
    discount_amount = p * (discount_per / 100)
    subtotal = p - discount_amount
    tax_amount = subtotal * (tax_per / 100)
    final_total = subtotal + tax_amount

    print(f"""
        "original_price": {p:.2f},
        "discount_amount": {discount_amount:.2f},
        "subtotal": {subtotal:.2f},
        "tax_amount": {tax_amount:.2f},
        "final_total": {final_total:.2f},
    """)

# Test with 100, 10% discount, 15% tax
calculate_bill(float(input("Enter The Price of Bill : ")))
