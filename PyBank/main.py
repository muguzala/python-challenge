import os
import csv
# open path
file_path = os.path.join('.', 'Resources', 'budget_data.csv')

budget_data = []

# Opening the CSV
with open(file_path) as csvfile:
    reader = csv.DictReader(csvfile)

    # Looping through the data to store in a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})
# Calculating the total months
total_months = len(budget_data)
# Looping through the dictionary in order to calculate changes between months
previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    prev_amount = budget_data[i]["amount"]
# Calculating the total amount
total_amount = sum(row['amount'] for row in budget_data) 
# Calculating the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months-1))
# Getting the  Greatest Increase and Decrease from the changes
def change(data):
    return data['change']
increase = max(budget_data, key=change)
decrease = min(budget_data, key=change)
# Printting the Final Analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
# exporting to a txt
filepath = os.path.join('.', 'Resources', 'PyBank_Results.txt')
with open(filepath, "w") as report:
    print('Financial Analysis', file=report)
    print('----------------------------', file=report)
    print(f'Total Months: {total_months}', file=report)
    print(f'Total: ${total_amount}', file=report)
    print(f'Average Change: ${average}', file=report)
