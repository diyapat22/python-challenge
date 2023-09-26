import csv

# Path to the CSV file inside the Resources folder
file_path = 'Resources/budget_data.csv'

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes = []
greatest_increase = {"Date": "", "Amount": float('-inf')}
greatest_decrease = {"Date": "", "Amount": float('inf')}

# Open and read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header
    header = next(csvreader)

    # Loop through each row of data
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        # Update total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_losses

        # Calculate the changes in profit/losses
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            # Check if the change is a new greatest increase or decrease
            if change > greatest_increase["Amount"]:
                greatest_increase["Date"] = date
                greatest_increase["Amount"] = change

            if change < greatest_decrease["Amount"]:
                greatest_decrease["Date"] = date
                greatest_decrease["Amount"] = change

        previous_profit_losses = profit_losses

# Calculate the average change in profit/losses
average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Losses: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})")

# Optionally, write the results to an output file
with open("financial_analysis_output.txt", "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total Profit/Losses: ${total_profit_losses}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})\n")
