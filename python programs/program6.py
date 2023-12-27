original_amount = int(input("Enter original amount: "))
discount_percentage = int(input("Enter discount percentage (int)(for eg, 20 for 20%): "))
discounted_amount = original_amount - (discount_percentage / 100) * original_amount
print("Discounted Amount:", discounted_amount)