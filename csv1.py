import csv

n1 = []
n2 = []
with open('Book1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #print ', '.join(row)
        n1.append(row);
i=0

for i in range(0, len(n1)):
    for k in n1[i]:
	n2.append(float(k))

print n2

i1 = []
i2 = []
with open('Book2.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        i1.append(row);
j=0

for j in range(0, len(i1)):
    for m in i1[i]:
        i2.append(float(m))

print i2
#a = list(map(int, a))
#a = [int(i) for i in a]

