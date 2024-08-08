# functions

# checks that an input was not left blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("This field must be filled")

        else:
            return response


# main
while True:
    name = not_blank("What is your name? ('x' to quit) ")

    if name == "x":
        break

    print("hello", name)
    print()

print("done")
