# Imports the os module, which allows creating file paths across operating systems
import os

# Imports csv module for reading csv files
import csv

# Reads the csv file into python
csvpath = os.path.join('Resources', 'election_data.csv')

# Establishes a variable to hold the total vote count
total_count = 0

# Establishes a list variable to hold the candidate names
candidates = []

# Establishes a list variable to hold the number of votes for each candidate
cand_votes = [0,0,0]

# Establishes a list variable to hold the perentage of votes for each candidate
cand_percent = []

# Establishes a variable for the winner
winner = 0

# Opens the csv path
with open(csvpath) as csvfile:

    # Defines the delimiter and variable for the data
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Defines the header for the csv file
    csv_header = next(csvreader)
    
    # Iterates through the rows of data in the csv file
    for row in csvreader:
        
        # Adds the candidates who recived votes to the candidates list
        if row[2] not in candidates:
            candidates.append(row[2])

        # totals each candidate's votes and writes to the candidate votes list
        if row[2] == candidates[0]:
            cand_votes[0] = cand_votes[0] + 1
        elif row[2] == candidates[1]:
            cand_votes[1] = cand_votes[1] + 1
        elif row[2] == candidates[2]:
            cand_votes[2] = cand_votes[2] + 1       

        # Sums the total votes by adding one while iterating through each row
        total_count = total_count + 1
        
        # Calculates each candidates percent of votes
        cand_percent = [100 * votes/total_count for votes in cand_votes]

    # Identifies the winner as the candidate with the most votes
    if cand_votes[0] > cand_votes[1] and cand_votes[2]:
        winner = candidates[0]
    elif cand_votes[1] > cand_votes[0] and cand_votes[2]:
        winner = candidates[1]
    elif cand_votes[2] > cand_votes[0] and cand_votes[1]:
        winner = candidates[2]

# Prints the Headers for the terminal printout
print("")
print("Election Results")
print("")
print("----------------------------")
print("")

# Prints the total votes for the terminal printout
print(f'Total Votes: {total_count}')
print("")
print("----------------------------")
print("")

# Prints the candidates, percentage of votes, and number of votes to the terminal printout from those lists
print(f'{candidates[0]}: {round(cand_percent[0],3)}% ({cand_votes[0]})')
print("")
print(f'{candidates[1]}: {round(cand_percent[1],3)}% ({cand_votes[1]})')
print("")
print(f'{candidates[2]}: {round(cand_percent[2],3)}% ({cand_votes[2]})')
print("")
print("----------------------------")
print("")

# Prints the winner to the the terminal printout
#print(f'Winner: ${winner)}')
print(f'Winner: {winner}')
print("")
print("----------------------------")
print("")


# Creates the text file for the results in the analysis folder
output_path = os.path.join("analysis", "results.txt")

# Opens the text file using "write" mode. Specifies the variable textfile to hold the contents
with open(output_path,'w') as textfile:
    # Prints the headers for the text file 
    textfile.write('\n')
    textfile.write("Election Results")
    textfile.write('\n')
    textfile.write("----------------------------")
    textfile.write('\n')

    # Writes the total votes to the text file
    textfile.write(f'Total Votes: {total_count}')
    textfile.write('\n')
    textfile.write("----------------------------")
    textfile.write('\n')
    
    # Writes the candidates, percentage of votes, and number of votes to the text file from those lists
    textfile.write(f'{candidates[0]}: {round(cand_percent[0],3)}% ({cand_votes[0]})')
    textfile.write('\n')
    textfile.write(f'{candidates[1]}: {round(cand_percent[1],3)}% ({cand_votes[1]})')
    textfile.write('\n')
    textfile.write(f'{candidates[2]}: {round(cand_percent[2],3)}% ({cand_votes[2]})')
    textfile.write('\n')
    textfile.write("----------------------------")
    textfile.write('\n')

    # Prints the winner to the text file
    textfile.write(f'Winner: {winner}')
    textfile.write('\n')
    textfile.write("----------------------------")
    textfile.write('\n')