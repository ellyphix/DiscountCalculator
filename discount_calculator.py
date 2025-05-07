def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        return price - discount
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values.")
