import csv
with open('primary-time-series.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count=0
    tally=0
    for row in spamreader:
        if count > 0:
            info=row[1].split(',')
            discharge=float(info[1])
            tally+=discharge
            #print(discharge)
        count+=1
    average=tally/(count-1)
    print(f"The mean is {average:.3f}")
    