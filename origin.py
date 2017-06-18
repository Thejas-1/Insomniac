import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB

n = []
n1 = []
with open('Book1.csv','rb') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #print ', '.join(row)
        n.append(row);
i=0

for i in range(0, len(n)):
    for k in n[i]:
        n1.append(float(k)) 
    
print n1



z = [] 
i1 = [] 
with open('Book2.csv','rb') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        z.append(row);

for i in range(0, len(z)):
    for m in z[i]:
        i1.append(float(m))

print i1


n = []
n2 = []
with open('Book3.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in spamreader:
        n.append(row);
k=0

for i in range(0, len(n)):
    for k in n[i]:
        n2.append(float(k))
 
print n2

z = []
i2 = []

with open('Book4.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|') 
    for row in spamreader:
        z.append(row);

for i in range(0, len(z)):
    for m in z[i]:
        i2.append(float(m))

print i2

X = np.array([n1,i1])
Y = np.array([1,0])

clf = GaussianNB()
clf.fit(X,Y)
print clf.predict([n2,i2])
