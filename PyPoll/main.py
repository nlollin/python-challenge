import os
import csv

file = os.path.join("Resources","election_data.csv")


with open(file,'r') as textio:
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    votes_total = len(list(csvreader))
    textio.seek(0)
    csvreader = csv.reader(textio,delimiter=',')
    csv_header = next(csvreader)

    candidates = []
    for row in csvreader: 
        candidates.append(row[2])

    unique_candidates = set(candidates)
    final_candidates = list(unique_candidates)
    number_of_votes = []
    vote_percentage = []
    x = 0

    print("Election Results")
    print("-------------------------------------")
    print("Total Votes: " +str(votes_total))
    print("-------------------------------------")
    
    for candidate in final_candidates: 
        
        
        vote_count = 0
        for element in candidates:
                if element == candidate:
                    vote_count = vote_count + 1
        number_of_votes.append(vote_count)
    
        vote_percentage.append(round((vote_count/votes_total)*100, 3))
        print(final_candidates[x] + ": " +str(vote_percentage[x])+ "% (" +str(number_of_votes[x])+ ")")
        x = x + 1


print("-------------------------------------")

most_votes = max(number_of_votes)
position = number_of_votes.index(most_votes)
winner = final_candidates[position]

print("Winner: " +winner)
print("-------------------------------------")

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