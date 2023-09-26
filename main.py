import csv


file_path = 'Resources/budget_data.csv'


total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes = []
greatest_increase = {"Date": "", "Amount": float('-inf')}
greatest_decrease = {"Date": "", "Amount": float('inf')}


with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    
    header = next(csvreader)

    
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        
        total_months += 1
        total_profit_losses += profit_losses

        
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            
            if change > greatest_increase["Amount"]:
                greatest_increase["Date"] = date
                greatest_increase["Amount"] = change

            if change < greatest_decrease["Amount"]:
                greatest_decrease["Date"] = date
                greatest_decrease["Amount"] = change

        previous_profit_losses = profit_losses


average_change = sum(changes) / len(changes)


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Losses: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})")




import csv


file_path = 'Resources/election_data.csv'


total_votes = 0
candidates = {}
winner = ''
highest_votes = 0


with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    
    header = next(csvreader)

    
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1


print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > highest_votes:
        highest_votes = votes
        winner = candidate

print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")


