import pandas
import random


# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index("Name")

# calculate the total ticket cost
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calculate profit for each of the tickets
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# choose a winner from name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won
total_won = mini_movie_frame.at[win_index, "Total"]

# set index at end
mini_movie_frame = mini_movie_frame.set_index("Name")
print(mini_movie_frame)

print("\n---- Raffle Winner ----")
print(f"Congrats {winner_name}. You have won ${total_won}, (your ticket is free)")
