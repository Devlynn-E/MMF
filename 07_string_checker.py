# functions
# checks the user entered a valid response based on a list of options
def string_checker(question, num_letters, valid_responses):

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(f"Please enter a valid response ({valid_responses[0]} or {valid_responses[1]})")


# main
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want instructions? ", 1, yes_no_list)

    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("\nhow would you like to pay? ", 2, payment_list)

    print("You chose", pay_method)
