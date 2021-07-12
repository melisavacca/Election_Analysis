#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = ("/Users/melis/OneDrive/Desktop/Bootcamp Class Folder/Election_Analysis/Resources/election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("..","Analysis", "election_Analysis.txt")

total_votes = 0

#candidate options
candidate_options = []
#declare the empty dictionay
candidate_votes = {}

#winnint candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        #print candidate name form each eow
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal.
    election_Analysis= (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_Analysis, end="")
    #save the final vote count to the text file. 
    txt_file.write(election_Analysis)

    #Determine the percentage of votes for each candidate
    #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = 
            #vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        #winning_candidate_summary = (
        #f"-------------------------\n"
        #f"Winner: {winning_candidate}\n"
        #f"Winning Vote Count: {winning_count:,}\n"
        #f"Winning Percentage: {winning_percentage:.1f}%\n"
        #f"-------------------------\n")

    #print(winning_candidate_summary)
    #To do: print out the winning candidate, vote count and percentage to the terminal.   
        #4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")

    #Print the candidate vote dictionary.
    #print(candidate_votes)

    #Print the candidate list.
    #print(candidate_options)


    #print(total_votes)

    #To do: perform analysis.
        #print(election_data)

    # Close the file.
        #election_data.close()

    # Using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save, "w")

    # #print out text to new election_analysis.txt
#outfile = open(file_to_save, "w")
    #outfile.write("Hello World")
    #outfile.close()

        #with open(file_to_save, "w") as txt_file:
        # Write three counties to the file.
            #txt_file.write("Arapahoe\nDenver\nJefferson")