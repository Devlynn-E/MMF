import pandas


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

# calculate the total ticket cost
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calculate profit for each of the tickets
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket and profit totals
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

# output table with ticket data
print(mini_movie_frame)

# output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
