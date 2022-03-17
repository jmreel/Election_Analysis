# The data we need to retrieve.
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()
with open(file_to_load) as election_data:
    print(election_data)
print(dir(os))
import os
dir(os)
dir(os.path)
os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    txt_file.write("Counties in the Election/n------------------------")

 # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.