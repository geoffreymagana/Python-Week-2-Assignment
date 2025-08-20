def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage to apply
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from user
try:
    original_price = float(input("Enter the original price of the item: KSh. "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if final_price != original_price:
        print(f"\nOriginal price: KSh. {original_price:.2f}")
        print(f"Discount applied: {discount_percentage}%")
        print(f"Final price after discount: KSh. {final_price:.2f}")
    else:
        print(f"\nNo discount applied. Final price: KSh. {final_price:.2f}")
        print("Note: Discount is only applied for discounts of 20% or higher.")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
