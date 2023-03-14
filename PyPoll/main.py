
import os
import csv

file_path = os.path.join('Resources', 'election_data.csv')

# Opening the CSV
with open(file_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]
    
total_votes = len(candidate_list)
canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Sorting the list so that the first candidate becomes the winner 
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


# save file in txt

filepath = os.path.join('.', 'Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as CSV_file:
    print("Election Results", file=CSV_file)
    print("-------------------------", file=CSV_file)
    print(f"Total Votes: {total_votes}", file=CSV_file)
    print("-------------------------", file=CSV_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f} % ({candidate[1]})', file=CSV_file)

    print("-------------------------", file=CSV_file)
    print(f"Winner: {canditates_info[0][0]}", file=CSV_file)
    print("-------------------------", file=CSV_file)
