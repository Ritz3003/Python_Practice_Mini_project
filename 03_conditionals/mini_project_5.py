# You run an online tea store, if order amount is more than 300 rupees delivery is free.
# Otherwise, delivery charge is 30 rupees. TASK :
# 1. Take input for order amount.
#2. use ternary operatior to decide the delivery fee.

order_amount = int(input("Enter the order amount : ")) # wrapping int converts here the input into integer if anything else can be written it throws error

#print(f"Order Amount : {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 30

print(f"delivery fees: {delivery_fees}")