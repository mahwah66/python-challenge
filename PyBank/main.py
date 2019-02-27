import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    
    totalmonths = 0
    nettotal = 0
    lastval = None
    deltas = []
    pmax = {"month":"", "val":0}
    lmin = {"month":"", "val":0}


    for row in csvreader:
        cmonth = row[0]
        cval = int(row[1])
        if (lastval != None):
            change = cval - lastval
            deltas.append(change)
            if (change > 0 and change > pmax["val"]):
                pmax["month"] = cmonth
                pmax["val"] = change
            elif (change < 0 and change < lmin["val"]):
                lmin["month"] = cmonth
                lmin["val"] = change
        nettotal += cval
        totalmonths += 1
        lastval = cval

    if len(deltas)>0:
        avgdelta = round(sum(deltas)/len(deltas), 2)
    else:
        avgdelta = "Error"
    
    toprint = "Financial Analysis" + os.linesep
    toprint += "---------------------------" +  os.linesep
    toprint += "Total Months:\t" + str(totalmonths) +  os.linesep
    toprint += "Total:\t" + '${:,.0f}'.format(nettotal) +  os.linesep
    toprint += "Average change:\t" + '${:,.2f}'.format(avgdelta) + os.linesep
    toprint += "Greatest Increase in Profits:\t" + pmax["month"]+ "\t" + "(" + '${:,.0f}'.format(pmax["val"]) + ")" + os.linesep
    toprint += "Greatest Decrease in Profits:\t" + lmin["month"]+ "\t" + "(" + '${:,.0f}'.format(lmin["val"]) + ")" + os.linesep
    
    print(toprint)

    resultsfile = open("results.txt","w+")
    resultsfile.write(toprint)
    resultsfile.close()