#A local cafe wants a program that suggests a snack.
#If a customer ask for cookies or samosa, which is a local Indian dish,
#it confirms the order, all right? Otherwise it says it's not available.
#TASK:
#1. Take snack input.
#2. if its "cookies" or "samosa", confirm order
#3. else show unavailability message.

snack = input("What would you like to order? : ").lower()

if snack == "cookies" or snack =="samosa":
    print(f"Great choice! {snack} is available. Your order is confirmed.")
else:
    print(f"Sorry we only server cookies and samosa with tea. {snack} is not available.")