import os
import csv

file = os.path.join("Resources","election_data.csv")


with open(file,'r') as textio:
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    #count the number of votes cast
    votes_total = len(list(csvreader))
    #return to the top of the csv file
    textio.seek(0)
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    #store the candidates name in a separate list (this will repeat each name as many times as it appears)
    candidates = []
    for row in csvreader: 
        candidates.append(row[2])

    #create a list that identify each candidate's name only once
    unique_candidates = set(candidates)
    final_candidates = list(unique_candidates)

    #start printing out the results
    print("Election Results")
    print("-------------------------------------")
    print("Total Votes: " +str(votes_total))
    print("-------------------------------------")

    #Set up lists to store the numbr of votes a candidate received & their respective vote percentage
    number_of_votes = []
    vote_percentage = []
    x = 0
    
    #loop through the list of unique candidates
    for candidate in final_candidates: 
        
        #set the starting vote count for each candidate
        vote_count = 0
        #loop through each row of the original candidate list that repeats the candidate name each time it appears
        for element in candidates:
                #for each candidate increase the vote count each time their name appears in the list
                if element == candidate:
                    vote_count = vote_count + 1
        #store the final vote count for each candidate in a separate list (in the same order the unique candidates names are listed in their list)
        number_of_votes.append(vote_count)
    
        #calculate the vote percentage for each candidate & print out the results for each candidate
        vote_percentage.append(round((vote_count/votes_total)*100, 3))
        print(final_candidates[x] + ": " +str(vote_percentage[x])+ "% (" +str(number_of_votes[x])+ ")")
        x = x + 1


print("-------------------------------------")

#identify the highest number of votes and the candidate associated with that vote count
#identify that candidate as the winner
most_votes = max(number_of_votes)
position = number_of_votes.index(most_votes)
winner = final_candidates[position]

#print a message identifying the winner
print("Winner: " +winner)
print("-------------------------------------")

#repeat the process print messages in a text file
with open("output.txt", "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------------------\n")
    f.write("Total Votes: " +str(votes_total) +"\n")
    f.write("-------------------------------------\n")

    for i in range(len(final_candidates)):
         f.write(final_candidates[i] + ": " +str(vote_percentage[i])+ "% (" +str(number_of_votes[i])+ ")\n")

    f.write("-------------------------------------\n")
    f.write("Winner: " +winner+ "\n")
    f.write("-------------------------------------\n")