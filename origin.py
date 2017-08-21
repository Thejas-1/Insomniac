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

#print n

for i in range(0, len(n)):
    for k in n[i]:
        n1.append(float(k)) 
    
#print n1



z = [] 
i1 = [] 
with open('Book2.csv','rb') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        z.append(row);

for i in range(0, len(z)):
    for m in z[i]:
        i1.append(float(m))

#print i1


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
 
#print n2

z = []
i2 = []

with open('Book4.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|') 
    for row in spamreader:
        z.append(row);

for i in range(0, len(z)):
    for m in z[i]:
        i2.append(float(m))

n=[]
n3=[]

with open('Normal/n1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in spamreader:
        n.append(row);

for i in range(0, len(n1)):
    for m in n[i]:
        n3.append(float(m))

#print n3

#print i2

z=[]
i3=[]

with open('insomniac/i1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in spamreader:
        z.append(row);

for i in range(0, len(n1)):
    for m in z[i]:
        i3.append(float(m))

a = []
b = []
c = []
d = []
e = []
f=[]
	
for i in range(0, (len(n1)-1)):
    a.append(n1[i+1]-n1[i])
    b.append(i1[i+1]-i1[i])
    c.append(n2[i+1]-n2[i])
    d.append(i2[i+1]-i2[i])
    e.append(n3[i+1]-n3[i])
    f.append(i3[i+1]-i3[i])

#for i in range(0, (len(n1-1)):

#print a
#print b
#print c
#print d
#b.append(0.0)
#d.append(0.0)

#print f

X = np.array([d,e,f])
Y = np.array([2,1,2])

clf = GaussianNB()
clf.fit(X,Y)
print clf.predict([c,b])                                 
