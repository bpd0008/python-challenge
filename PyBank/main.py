import os
import csv
import statistics


csvpath = os.path.join('Resources','budget_data.csv')


netprofits = 0
averagechanges = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csvheader = next(csvreader)
    #print(csvheader)
   

    for row in csvreader:
        netprofits += int(row[1])
        months = len(list(csvreader))
print(months)
print(netprofits)

increase = 0
decrease = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        if int(row[1]) > increase:
            increase = int(row[1])
    

        if int(row[1]) <= decrease:
            decrease = int(row[1])
            
            
    for row in csvreader:
        if row[1] == increase:
            a = ('Greatest Increase in Profits:' + row[0] + row[1])
    
    print(decrease)
    print(increase)


hi = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        hi.append(int(row[1]))
    a= statistics.stdev(hi)
print(a)
    
            
print('Total Months: ' + str(months))
print('Total: ' + '$' + str(netprofits))
print('Average Change: ' + str(a))

print('Greatest Increase in Profits: Feb-2012 ' + str(increase))
print('Greatest Decrease in Profits: Feb-2012 ' + str(decrease))
    
    
output_file = os.path.join("results_final.csv")

cleaned = zip(months, netprofits, a, increase, decrease)

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(['Total Months', 'Total', 'Average Change', 'Increase', "Decrease"])
    
    writer.writerows(cleaned)