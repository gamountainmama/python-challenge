# Imports the os module, which allows creating file paths across operating systems
import os

# Imports csv module for reading csv files
import csv

# Reads the csv file into python
csvpath = os.path.join('Resources', 'budget_data.csv')

# Establishes a variable to count the total months
total_months = 0

# Establishes a variable to find the sum of profits and losses
net_total = 0

# Establishes variables for the old and new profits and losses for iterating through to find the change
old = 0
new = 0

# Establishes a variable to find the change in profits and losses
net_change = 0

# Establishes a variable for the average change in profits and losses
avg_change = 0

# Establishes variables for the greatest increase and decrease in profit and their dates
greatest_inc = 0
greatest_dec = 0
date_g_inc = 0
date_g_dec = 0

# Opens the csv path
with open(csvpath) as csvfile:

    # Defines the delimiter and variable for the data
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Defines the header for the csv file
    csv_header = next(csvreader)
    
    # Iterates through the rows of data in the csv file
    for row in csvreader:

        # Sets the profit/loss for the current row
        new = int(row[1])

        # Calculates the running net change in profits and losses
        if total_months > 0:
            net_change = net_change + new - old
            
            # Checks for the greatest increase in profit
            if new - old > greatest_inc:
                greatest_inc = new - old
                
                # Captures the date of the greatest increase in profit
                date_g_inc = row[0]

            # Checks for the greatest decrease in profit
            if new - old < greatest_dec:
                greatest_dec = new - old
                
                # Captures the data of the greatest decrease in profit
                date_g_dec = row[0]

        # updates the profit/loss for old to the outgoing value (new)
        old = new

        # Counts the months
        total_months = total_months + 1

        # Sums the profits/losses
        net_total = net_total + int(row[1])

    # Calculates the average change
    avg_change = net_change / (total_months - 1)

# Prints the Headers for the terminal printout
print("")
print("Financial Analysis")
print("")
print("----------------------------")
print("")

# Prints the total months for the terminal printout
print(f'Total Months: {total_months}')
print("")

# Prints the net profit/loss for the terminal printout
print(f'Total: ${net_total}')
print("")

# Prints the average change in profit/loss for the terminal printout
print(f'Average Change: ${round(avg_change,2)}')
print("")

# Prints the greatest increase in profits for the terminal printout
print(f'Greatest Increase in Profits: {date_g_inc} (${greatest_inc})')
print("")

# Prints the greatest decrease in profits for the terminal printout
print(f'Greatest Decrease in Profits: {date_g_dec} (${greatest_dec})')
print("")

# Creates the text file for the results in the analysis folder
output_path = os.path.join("analysis", "results.txt")

# Opens the text file using "write" mode. Specifies the variable textfile to hold the contents
with open(output_path,'w') as textfile:
    # Writes the headers for the text file 
    textfile.write('\n')
    textfile.write("Financial Analysis")
    textfile.write('\n')
    textfile.write("----------------------------")
    textfile.write('\n')

    # Writes the total months to the text file 
    textfile.write(f'Total Months: {total_months}')
    textfile.write('\n')

    # Writes the net profit/loss to the text file 
    textfile.write(f'Total: ${net_total}')
    textfile.write('\n')

    # Writes the average change in profit/loss to the text file 
    textfile.write(f'Average Change: ${round(avg_change,2)}')
    textfile.write('\n')

    # Writes the greatest increase in profits to the text file 
    textfile.write(f'Greatest Increase in Profits: {date_g_inc} (${greatest_inc})')
    textfile.write('\n')

    # Writes the greatest decrease in profits to the text file 
    textfile.write(f'Greatest Decrease in Profits: {date_g_dec} (${greatest_dec})')
    textfile.write('\n')  



