# functions

# checks if a response was yes or no
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


# checks that an input was not left blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("This field must be filled")

        else:
            return response


# checks that the user entered a number within given parameters, or an exit code
def num_check(question, low=12, high=120, exit_code="x"):

    while True:

        response = input(question)

        if response == exit_code:
            result = "x"
            break

        try:
            num = int(response)

            if low <= num <= high:
                result = num
                break

            elif num < low:
                print("you're too young")

            elif num > high:
                print("you may have made a typo, try again")

            else:
                print(f"Please input an integer between {low} and {high}")

        except ValueError:
            print("Please enter an integer, or 'x' to quit")

    return result


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

# set default settings
max_tickets = 3
tickets_sold = 0

# asks if user wants instructions
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print("\ninstructions")

# loop to sell all tickets
while tickets_sold < max_tickets:

    # asks user for their name, if user inputs exit code, code stops.
    name = not_blank("\nWhat is your name? ('x' to quit) ")

    if name == "x":
        break

    # asks the user for their age (has exit code)
    age = num_check(f"\n{name}, please enter your age: ")

    if age == "x":
        break

    # calculates the cost of the ticket
    ticket_cost = ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")

    # adds to the total of tickets sold
    tickets_sold += 1

# output sold tickets
if tickets_sold == max_tickets:
    print("you sold all of your tickets")

else:
    print(f"You sold {tickets_sold} ticket/s. you still have {max_tickets - tickets_sold} ticket/s to sell")
