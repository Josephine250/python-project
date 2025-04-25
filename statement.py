def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
orig_price = float(input("enter original price :"))  
disc_percentage = float(input("enter disc percentage :"))   
final_price = calculate_discount(orig_price,disc_percentage)
if disc_percentage >= 20:
     print("final_price is :",final_price)
else:
     print("original price is :",orig_price)