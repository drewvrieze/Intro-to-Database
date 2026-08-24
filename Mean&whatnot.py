import csv
import math

#calculates average
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

#Calculates min and max
with open('primary-time-series.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count=0
    tally=0
    minimum = average
    maximum = average
    for row in spamreader:
        if count > 0:
            info = row[1].split(',')
            discharge = float(info[1])
            if discharge < minimum:
                minimum = discharge
            if discharge > maximum:
                maximum = discharge
        count += 1
    print(f"The maximum is {maximum:.3f}")
    print(f"The minimum is {minimum:.3f}")

#calculates standard deviation
with open('primary-time-series.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count=0
    tally=0
    sdcounter = 0
    for row in spamreader:
        if count > 0:
            info = row[1].split(',')
            discharge = float(info[1])
            sdcounter += (discharge-average)**2
        count += 1
    sd = math.sqrt(sdcounter/(count-2))
    print(f"The standard deviation is {sd:.3f}")
