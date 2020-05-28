import os
import csv
import math

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    month_count = []
    net_profit = []
    average_change = []

    for row in csvreader:
        month_count.append(row[0])
        net_profit.append(int(row[1]))
    
    for i in range(len(net_profit)-1):
        average_change.append(net_profit[i+1]-net_profit[i])
        
most_profit = max(average_change)
most_loss = min(average_change)

date_profit = average_change.index(max(average_change))
date_loss = average_change.index(min(average_change))

print(f"Financial Analysis")
print(f"----------------------------\n")
print(f"Total Months: {len(month_count)}\n")
print(f"Total: ${sum(net_profit)}\n")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}\n")
print(f"Greatest Increase in Profits: {month_count[date_profit]} (${(str(most_profit))})\n")
print(f"Greatest Decrease in Profits: {month_count[date_loss]} (${(str(most_loss))})\n")

file = 'summary.txt'

with open(file, 'w') as text:
    print(text)
    formatTxt = (
                f"Financial Analysis\n"
                f"----------------------------\n"
                f"Total Months: {len(month_count)}\n"
                f"Total: ${sum(net_profit)}\n"
                f"Average Change: {round(sum(average_change)/len(average_change),2)}\n"
                f"Greatest Increase in Profits: {month_count[date_profit]} (${(str(most_profit))})\n"
                f"Greatest Decrease in Profits: {month_count[date_loss]} (${(str(most_loss))})\n"
    )
    text.write(formatTxt)    
    
