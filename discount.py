# Draft by Tatenda Felix Mukaro || 26 April 2021 || Week 2 Team Project

# The following code imports the datetime function from the 
#python library and uses some of its objects
from datetime import datetime
current = datetime.now()
weekday = current.isoweekday()
print(weekday)
#print (current)

# The following code prompts the user for the subtotal input
sub_total = float(input("Please enter the subtotal: "))

# This section performs the tax and discounted amount calculations
# Given discount is 10% and Tax is 6%
calculate_discount = 0.1 * sub_total
discounted_amount = (sub_total - calculate_discount)

calculate_tax1 = 0.06 * discounted_amount
calculate_tax2 = 0.06 * sub_total

final_subtotal1 = discounted_amount + calculate_tax1
final_subtotal2 = sub_total + calculate_tax2

# The following conditional statements help to check for 
# the required tuesday, wednesday parametres
# The print statements, outputs the text written in strings
if ((weekday == 2 or weekday == 3) and sub_total >= 50 ):
    print(f"Discount amount: {calculate_discount: .2f}") 
    print(f"Sales tax amount: {calculate_tax1: .2f}")
    print(f"Total: {final_subtotal1: .2f}")


elif (weekday == 2 and weekday == 3 and sub_total < 50):
    print(f"Sales tax amount:{calculate_tax2: .2f}")
    print(f"Total: {final_subtotal2: .2f}")
    
else:
    print(f"Sales tax amount:{calculate_tax2: .2f}")
    print(f"Total: {final_subtotal2: .2f}")
 
