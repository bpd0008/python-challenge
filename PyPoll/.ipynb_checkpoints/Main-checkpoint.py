
import csv
import os


file = 'Resources/election_data.csv'
filej = os.path.join(file)

a = []
candidates = []
khan = []
correy = []
li = []
tooley = []

with open(filej) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        a.append(row[1])
        
        
        if row[2] == 'Khan':
            khan.append(list(candidates))
            
        if row[2] == 'Correy':
            correy.append(list(candidates))
            
        if row[2] == 'Li':
            li.append(list(candidates))
            
        if row[2] == "O'Tooley":
            tooley.append(list(candidates))
            
print(len(a))
print(len(khan))
print(len(correy))
print(len(li))
print(len(tooley))



k = 0
c = 0
l = 0
t = 0

k = round((len(khan)/len(a)), 2)
pk = "{:.0%}".format(k)

c = round((len(correy)/len(a)), 2)
pc = "{:.0%}".format(c)

l = round((len(li)/len(a)), 2)
pl = "{:.0%}".format(l)


t = round((len(tooley)/len(a)), 2)
pt = "{:.0%}".format(t)

print(pk)
print(pc)
print(pl)
print(pt)

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(len(a)))
print('-------------------------')
print('Khan: ' + str(pk) + ' ' + str(len(khan)))
print('Correy: ' + str(pc) + ' '  + str(len(correy)))
print('Li: ' + str(pl) + ' '  + str(len(li)))
print("O'Tooley: " + str(pt) + ' '  + str(len(tooley)))
print('-------------------------')
print('Winner: Khan')
print('-------------------------')cleaned = zip(a, pk, pc, pl, pt)

output_file = os.path.join("results_final.csv")


with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(['Total', 'Khan_Percentage', 'Correy_Percentage', 'Li_Percentage', "O'Tooley_Percentage"])
    
    writer.writerows(cleaned)
    