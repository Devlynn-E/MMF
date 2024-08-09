# functions

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


# main
tickets_sold = 0
max_tickets = 10

while tickets_sold < max_tickets:
    name = input("\nEnter your name / x to quit: ")

    if name == "x":
        break

    age = num_check(f"\n{name}, please enter your age: ")

    if age == "x":
        break

    tickets_sold += 1

if tickets_sold == max_tickets:
    print("\nyou sold all the tickets")

else:
    print(f"\nyou sold {tickets_sold} ticket/s you still have to sell {max_tickets - tickets_sold} ticket/s")

print("\ndone")
