# function
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


# main
while True:
    want_instructions = yes_no("Do you want to see instructions? ")

    if want_instructions == "yes":
        print("instructions")

    print("<continue>")
    print()
