# main

# set max tickets
max_tickets = 3

# loop to sell
tickets_sold = 0
while tickets_sold < max_tickets:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    tickets_sold += 1

# output sold tickets
if tickets_sold == max_tickets:
    print("you sold all of your tickets")

else:
    print(f"You sold {tickets_sold} ticket/s. you still have {max_tickets - tickets_sold} ticket/s to sell")
