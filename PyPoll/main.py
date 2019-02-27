import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    candidates = {}
    totalvotes = 0

    for row in csvreader:
        totalvotes += 1
        cand = row[2]
        if cand in candidates:
            candidates[cand] = candidates[cand] + 1
        else:
            candidates[cand] = 1
    
    hr = "-----------------------------" + os.linesep
    toprint = "Election Results" + os.linesep + hr
    toprint += "Total Votes:  " + str(totalvotes) + os.linesep + hr

    for cand in candidates:
        toprint += cand + ":  " + str(round(100*candidates[cand]/totalvotes, 3)) + "%    (" + str(candidates[cand]) + ")" + os.linesep
    
    toprint += hr + "Winner:  " + max(candidates, key=candidates.get) + os.linesep + hr
    print(toprint)

    resultsfile = open("results.txt","w+")
    resultsfile.write(toprint)
    resultsfile.close()







