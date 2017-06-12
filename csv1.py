import csv

a = []
b = []
with open('Book1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #print ', '.join(row)
        a.append(row);
i=0

for i in range(0, len(a)):
    for k in a[i]:
	b.append(float(k))

print b

c = []
d = []
with open('Book2.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        c.append(row);
j=0

for j in range(0, len(a)):
    for m in c[i]:
        d.append(float(m))

print d
#a = list(map(int, a))
#a = [int(i) for i in a]

