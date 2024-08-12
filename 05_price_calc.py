# functions

# calculate the ticket price based on age
def ticket_price(var_age):

    if var_age < 16:
        price = 7.50

    elif 16 <= var_age < 65:
        price = 10.50

    else:
        price = 6.50

    return price


# main
while True:

    # get age
    age = int(input("Age: "))

    # calculate cost
    ticket_cost = ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")
