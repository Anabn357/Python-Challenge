import os
import csv
import math

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print("Evaluating Poll")
    print("---------------------------")

    header = next(csvreader)

    khan_count = 0
    khan_percent = 0.00
    correy_count = 0
    correy_percent = 0.00
    li_count = 0
    li_percent = 0.00
    otooley_count = 0
    otooley_percent = 0.00
    winner_count = 0
    count_total = 0
    winner = ""
  

    for row in csvreader:
        count_total = count_total + 1
        if(row[2] == "Khan"):
            khan_count = khan_count + 1
        elif(row[2] == "Correy"):
            correy_count = correy_count + 1
        elif(row[2] == "Li"):
            li_count = li_count + 1
        elif(row[2] == "O'Tooley"):
            otooley_count = otooley_count + 1

    khan_percent = khan_count / count_total * 100
    correy_percent = correy_count / count_total * 100
    li_percent = li_count / count_total * 100
    otooley_percent = otooley_count / count_total * 100

winner_count = max(khan_count, correy_count, li_count, otooley_count)
if(winner_count == khan_count):
    winner = "Khan"
elif(winner_count == correy_count):
    winner = "Correy"
elif(winner_count == li_count):
    winner = "Li"
else:
    winner = "O'Tooley"

print(count_total)

print(
        f"Election Results\n"
        f"---------------------------------\n"

        f"Total Votes: {str(count_total)}\n"
        f"---------------------------------\n"

        f"Khan: {str(khan_percent)} %\n"
        f"({str(khan_percent)})\n" 

        f"Correy: {str(correy_percent)} %\n"
        f"({str(correy_percent)})\n" 

        f"Li: {str(li_percent)} %\n"
        f"({str(li_percent)})\n" 

        f"O'Tooley: {str(otooley_percent)} %\n"
        f"({str(otooley_percent)})\n" 

        f"---------------------------------\n"

        f"Winner: {str(winner)}\n"
        
        f"---------------------------------\n"
    )


file = 'poll.txt'
with open(file, 'w') as text:
    print(text)
    formatTxt = (
        f"Election Results\n"
        f"---------------------------------\n"

        f"Total Votes: {str(count_total)}\n"
        f"---------------------------------\n"

        f"Khan: {str(khan_percent)} %\n"
        f"({str(khan_percent)})\n" 

        f"Correy: {str(correy_percent)} %\n"
        f"({str(correy_percent)})\n" 

        f"Li: {str(li_percent)} %\n"
        f"({str(li_percent)})\n" 

        f"O'Tooley: {str(otooley_percent)} %\n"
        f"({str(otooley_percent)})\n" 

        f"---------------------------------\n"

        f"Winner: {str(winner)}\n"
        
        f"---------------------------------\n"
    )
    text.write(formatTxt)

