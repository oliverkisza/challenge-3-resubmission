import csv
from pathlib import Path

#read csv and put in list
data = []
csvpath = Path('python-challenge-3/PyPoll/Resources/election_data.csv')
with csvpath.open('r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ballot_id, county, candidate = row
        data.append((ballot_id, county, candidate))

total_votes = len(data)

candidates = []
candidate_votes = {}
for _, _, candidate in data:
    if candidate not in candidates:
        candidates.append(candidate)
        candidate_votes[candidate] = 1
    else:
        candidate_votes[candidate] += 1

    candidate_percents = {}
    winner = candidates[0]

for candidate in candidates:
    percentage = (candidate_votes[candidate]/ total_votes) * 100
    candidate_percents[candidate] = percentage
    if candidate_votes[candidate] > candidate_votes[winner]:
        winner = candidate

#print to terminal
print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes))
print("---------------------")
print("Percentage of votes each candidate won:")
print(candidates[1] + ": " + str(round(candidate_percents[candidates[1]], 3)) + "%" + " (" + str(candidate_votes[candidates[1]]) + ")")
print(candidates[2] + ": " + str(round(candidate_percents[candidates[2]], 3)) + "%" + " (" + str(candidate_votes[candidates[2]]) + ")")
print(candidates[3] + ": " + str(round(candidate_percents[candidates[3]], 3)) + "%"+ " (" + str(candidate_votes[candidates[3]]) + ")")
print("---------------------")
print("Winner: " + winner)
print("---------------------")

#output to analysis2.txt file
with open("Analysis2.txt", "w") as output:
    print("Election Results", file=output)
    print("---------------------", file=output)
    print("Total Votes: " + str(total_votes), file=output)
    print("---------------------", file=output)
    print("Percentage of votes each candidate won:", file=output)
    print(candidates[1] + ": " + str(round(candidate_percents[candidates[1]], 3)) + "%" + " (" + str(candidate_votes[candidates[1]]) + ")", file=output)
    print(candidates[2] + ": " + str(round(candidate_percents[candidates[2]], 3)) + "%" + " (" + str(candidate_votes[candidates[2]]) + ")", file=output)
    print(candidates[3] + ": " + str(round(candidate_percents[candidates[3]], 3)) + "%"+ " (" + str(candidate_votes[candidates[3]]) + ")", file=output)
    print("---------------------", file=output)
    print("Winner: " + winner, file=output)
    print("---------------------", file=output)