#create variables
total_votes = 0
candidates = {}  # dictionary to store candidate names as keys and their vote counts as values
winner = ""
winner_votes = 0

#define output file location and filename
OutputFile = "C:/Users/baseb/OneDrive/Desktop/Data Analytics Course/Module 3/python-challenge/PyPoll/analysis/analysis.txt"

#read CSV file
with open('/Users/baseb/OneDrive/Desktop/Data Analytics Course/Module 3/python-challenge/PyPoll/Resources/election_data.csv','r') as csvfile:

    header = next(csvfile) # skips header row
   
    for line in csvfile :
        #split column into three columns
        Ballot_ID, County, CandidateRow = line.strip().split(',')

        #count votes
        total_votes += 1
        
        #count votes for each candidate 
        if CandidateRow in candidates:
            candidates[CandidateRow] += 1
        else:
            candidates[CandidateRow] = 1
    
#prints results to txt file and terminal
with open(OutputFile, "w") as OutputFile:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    OutputFile.write("Election Results\n")
    OutputFile.write("-------------------------\n")
    OutputFile.write(f"Total Votes: {total_votes}\n")
    OutputFile.write("-------------------------\n")
    
    #find winner and percentages
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100

        print(f"{candidate}: {percentage:.3f}% ({votes})")
        OutputFile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        if votes > winner_votes:
            winner = candidate
            winner_votes = votes
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    OutputFile.write("-------------------------\n")
    OutputFile.write(f"Winner: {winner}\n")
    OutputFile.write("-------------------------\n")

# lets us know results were printed in txt file.
print(f"Results have been saved to {OutputFile}")