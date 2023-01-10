import os

# Module for reading CSV files
import csv

# Module for statistics - easier than doing the math!
import statistics

# here's my election data - it's in a folder called resources in that lives at the same level as main.py
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')


monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''



change = []
monthToMonthChange = []

with open(budget_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        monthCount += 1
        totalVolume += int(row[1])
        if int(row[1]) > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))

  
# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Total: $" + str(totalVolume))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

