#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load=os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to the path
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Add total_votes variable
total_votes=0

#Candidate options
candidate_options=[]

#Declare dictionary
canidate_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add the total vote count
        total_votes +=1

        #Print the candidate name from each row
        canidate_name=row[2]

        #If the candidate does not match the existing candidate
        if canidate_name not in candidate_options:
           candidate_options.append(canidate_name)

           #Begin tracking votes
           canidate_votes[canidate_name]=0

        #Add votes to candidate's count
        canidate_votes[canidate_name] +=1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        #Save the final vote count to the text file
    txt_file.write(election_results)

    #Determine the percentage of botes for each candidate
    #Iterate through the candidate list
    for candidate_name in canidate_votes:
        #Retrieve vote count of a candidate
        votes=canidate_votes[candidate_name]
        #Calcualte percentage
        vote_percentage=float(votes)/float(total_votes)*100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to terminal.
        print(candidate_results)
        #Save candidate resultes to text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)