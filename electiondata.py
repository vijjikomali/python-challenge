import csv
import os
os.chdir('C:/Users/Vijayalaskmi/Desktop/ROOT FOLDER/PREWORK-VJK/MODULE3/homework')

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Output", "election.txt")
print(os.getcwd())
# we have to initialize some variables so that we can run the loop when we create!
# read csv file and convert into dictioneries of list

with open(file_to_load, newline="") as election_data:
    reader =  csv.reader(election_data)
    header = next(reader)

    # variables list
    tally_votes = []
    khan_votes = 0
    corey_votes = 0
    li_votes = 0
    otley_votes = 0

# running a loop to get 
    for row in reader:
# counting total votes
        tally_votes.append(row[0])
    # number of candidates located in the list by individual total
        if row[2] == "Khan":
            khan_votes+= 1
        elif row[2] == "Correy":
            corey_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otley_votes += 1

#print the total votes for th individual
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, corey_votes,li_votes,otley_votes]

#print(votes)
# creating dictionaries
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# finding the percerntage of each candidates

khan_percent = (khan_votes/len(tally_votes)) *100
correy_percent = (corey_votes/len(tally_votes)) * 100
li_percent = (li_votes/len(tally_votes))* 100
otooley_percent = (otley_votes/len(tally_votes)) * 100
        

#prints the total results Q1, Q2, Q3,Q4,Q5
# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {len(tally_votes)}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({corey_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# printing the textfile 
file = open(file_to_output, "w+")
file.write(f"Election Results")
file.write("\n")
file.write(f"----------------------c------")
file.write("\n")
file.write(f"Total Votes: {len(tally_votes)}")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
file.write("\n")
file.write(f"Correy: {correy_percent:.3f}% ({corey_votes})")
file.write("\n")
file.write(f"Li: {li_percent:.3f}% ({li_votes})")
file.write("\n")
file.write(f"O'Tooley: {otooley_percent:.3f}% ({otley_votes})")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Winner: {key}")
file.write("\n")
file.write(f"----------------------------")

