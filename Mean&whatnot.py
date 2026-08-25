import csv

#calculates average
with open('primary-time-series.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count=0
    tally=0
    tally=0
    tallysq=0
    measure = []
    for row in spamreader:
        if count > 0:
            info=row[1].split(',')
            discharge=float(info[1])
            tally+=discharge
            measure.append(discharge)
            tallysq += discharge * discharge
            #print(discharge)
        count+=1

    smeasure = sorted(measure)
    p25 = smeasure[int((count-1)*0.25)]
    p50 = smeasure[int((count-1)*0.50)]
    p75 = smeasure[int((count-1)*0.75)]
    average=tally/(count-1)
    variance = tallysq/(count - 1) - average * average
    stdev = (variance)**(0.5)
    # print (f"{stdev:.4f}")
    print(p25,p50,p75)


#Calculates min and max
# with open('primary-time-series.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     count=0
#     tally=0
#     minimum = average
#     maximum = average
#     for row in spamreader:
#         if count > 0:
#             info = row[1].split(',')
#             discharge = float(info[1])
#             if discharge < minimum:
#                 minimum = discharge
#             if discharge > maximum:
#                 maximum = discharge
#         count += 1
#     print(f"The maximum is {maximum:.3f}")
#     print(f"The minimum is {minimum:.3f}")

#calculates standard deviation
# with open('primary-time-series.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     count=0
#     tally=0
#     sdcounter = 0
#     for row in spamreader:
#         if count > 0:
#             info = row[1].split(',')
#             discharge = float(info[1])
#             sdcounter += (discharge-average)**2
#         count += 1
#     sd = (sdcounter/(count-2))**(0.5)

    print(f"The mean is {average:.4f}.\nThe min is {min(measure)}.\nThe maximum is {max(measure)}.\nThe standard deviation is {stdev:.4f}.")
