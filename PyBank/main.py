# Creating the file
import os
# Reading the CSV file
import csv
# Statistics
import statistics
# Opening the CSV
with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
# Defining variables
    next(csv_reader)
    total_months = 0
    net_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    best_Month = ""
    worst_Month = ""
    change = []
    monthToMonthChange = []
    monthly_change = 0
 #Looping   
    for row in csv_reader:
        print(row)
        total_months += 1
        net_total += int(row[1])
        monthly_change = int(row[1]) - monthly_change
        change.append(monthly_change)
        if monthly_change > greatest_increase:
           best_Month = (row[0])
           greatest_increase = monthly_change
        elif monthly_change < greatest_decrease:
           worst_Month = (row [0])
           greatest_decrease = monthly_change
        monthly_change = int(row[1])
        

#Results      
print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average Change is: $" + str( round(statistics.mean(change[1:]), 2)))
print("Greatest Increase in Profits: " + str(best_Month) + "  ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_Month) + "  ($" + str(greatest_decrease) + ")")
# Output file
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(total_months))
f.write("Average Change is: $" + str( round(statistics.mean(change[1:]), 2)))
f.write("Total: $" + str(net_total))
f.write("Greatest Increase in Profits: " + str(best_Month) + "  ($" + str(greatest_increase) + ")")
f.write("Greatest Decrease in Profits: " + str(worst_Month) + "  ($" + str(greatest_decrease) + ")")
