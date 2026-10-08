age = int(input("Enter your age: "))
day = input("Enter the day: ")
student = input("Are you a student? (yes/no): ")

if age < 0:
    print("Invalid age")

elif day != "Monday" and day != "Tuesday" and day != "Wednesday" and \
     day != "Thursday" and day != "Friday" and day != "Saturday" and \
     day != "Sunday":
    print("Invalid day")

else:
    if age < 5:
        price = 0
    elif age <= 12:
        price = 6
    elif age <= 59:
        price = 10
    else:
        price = 7

    if day == "Friday" and price > 0:
        price += 2

    if student == "yes" and price > 0:
        price *= 0.80

    price = round(price, 2)

    if price == 0:
        print("Ticket price: Free")
    else:
        print("Ticket price: $", price)
