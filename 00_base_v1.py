# imports
import pandas
import random


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


# format into currency
def currency(x):
    return f"${x:.2f}"


# main

# set default settings
max_tickets = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

# Dictionary used to create data frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharges
}

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

    if pay_method == "cash":
        surcharge = 0
    else:
        # 5% of ticket cost as surcharge for using credit
        surcharge = ticket_cost * 0.05

    # adds to the total of tickets sold
    tickets_sold += 1

    # append names, ticket costs, and surcharge to each of the lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharges.append(surcharge)


mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index("Name")

# calculate the total ticket cost
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calculate profit for each of the tickets
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket and profit totals
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

# currency formatting
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose a winner from name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won
total_won = mini_movie_frame.at[win_index, "Total"]

# checks that there is data within the table
if mini_movie_frame["Total"].sum() == 0:
    print("No data for the table")

else:
    print("\n------ Ticket Data ------")
    print()

    # output table with ticket data
    print(mini_movie_frame)

    print("\n----- Ticket Cost / Profit -----")

    # output total ticket sales and profit
    print(f"Total Ticket Sales: ${total:.2f}")
    print(f"Total Profit: ${profit:.2f}")

    print("\n---- Raffle Winner ----")
    print(f"Congrats {winner_name}. You have won {total_won}, (your ticket is free)")


# output sold tickets
if tickets_sold == max_tickets:
    print("\nyou sold all of your tickets")

else:
    print(f"\nYou sold {tickets_sold} ticket/s. you still have {max_tickets - tickets_sold} ticket/s to sell")
