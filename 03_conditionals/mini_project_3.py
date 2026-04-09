#We have a Tea stall which offers different prices for different cup sizes.
#Write a program that calculates the price based on the size.
#TASK:
#1. Take input for cup size (small, medium, large)
#2. if small show price 10, if medium show price 20, if large show price 30
#3. if the input is not valid, show "Invalid size. Please choose small, medium, or large."

cup_size = input("Welcome to Ritu's Tea stall! please tell me your prefered cup size) : ").lower()

if cup_size == "small":
    print(f"{cup_size} cup is for Rs: 10")
elif  cup_size == "medium":
    print(f"{cup_size} cup is for Rs: 20")
elif cup_size == "large":
    print(f"{cup_size} cup is for Rs: 30")
else:
    print(f"{cup_size} is invalid size. please choose small, medium or large. ")


   