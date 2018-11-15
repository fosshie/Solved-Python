# import os and write csv path
# Improved Reading using CSV module
from statistics import mean
import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")



with open(csvpath, newline='') as csvfile:
    # CSV reader delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    csvlist = list(csvreader)

    # list creation, places to store csv "rows" (They are columns!)
    dates = []
    revenues = []

    # run for loop for every row
    for dog in csvlist:
        dates.append(dog[0])
        revenues.append(int(dog[1]))

    # create a list for revenue change
    revchange = []

    # run loop through revenues list to find the change revenues from month
    revchange = [revenues[i + 1] - revenues[i] for i in range(len(revenues) - 1)]

    # variables
    max_change = max(revchange)
    min_change = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    max_month = None
    min_month = None


    # for loop to find corresponding date
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == min_change:
            min_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])

    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_month} ${max_change}")
    print(f"Greatest Decrease in Profits: {min_month} ${min_change}")
