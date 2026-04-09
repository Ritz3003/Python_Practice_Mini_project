# you are building a ticket info system for a Railway app
# Based on seat type show its feature TASK:
# INPUT : seat_type = "sleeper","AC", "general","Luxury"
# Match using match case
# Unknown seat type should show "Invalid seat type"

seat_type = input("please tell me your seat type (sleeper/AC/general/Luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("Non AC with beds reservation required")
    case "ac":
        print("AC with beds reservation required")
    case "general":
        print("cheapest, Non Ac, No Beds and no reservation")
    case "luxury":
        print("luxury, AC, beds with meal and reservation needed")
    case _:
        print("Invalid seat type!!")