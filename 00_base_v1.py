# functions

# checks the user entered a valid response based on a list of options
def string_checker(question, num_letters, valid_responses):

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(f"Please enter a valid response ({valid_responses[0]} or {valid_responses[1]})")


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

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# asks if user wants instructions
want_instructions = string_checker("Do you want to see the instructions? ", 1, yes_no_list)

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

    # get payment method
    pay_method = string_checker("\nhow would you like to pay? ", 2, payment_list)

    # adds to the total of tickets sold
    tickets_sold += 1

# output sold tickets
if tickets_sold == max_tickets:
    print("you sold all of your tickets")

else:
    print(f"You sold {tickets_sold} ticket/s. you still have {max_tickets - tickets_sold} ticket/s to sell")
