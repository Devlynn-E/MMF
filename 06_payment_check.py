# function
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("please choose a valid payment type")


# main
while True:
    payment_type = cash_credit("Paying with cash or credit? ")

    if payment_type == "cash":
        print("You're paying with cash")

    else:
        print("You're paying with credit")

    print("<continue>")
    print()
