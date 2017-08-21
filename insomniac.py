import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB

n = []
n1 = []
with open('Book1.csv','rb') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
#        print ', '.join(row)
        n.append(row);
i=0

#print n

for i in range(0, len(n)):
    for k in n[i]:
        n1.append(float(k)) 
    
#print n1


def i1():
    z = [] 
    i1 = [] 
    with open('Book2.csv','rb') as csvfile: 
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(z)):
        for m in z[i]:
            i1.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i1[i+1]-i1[i])
    return a

#n = []
#n2 = []
#with open('Book3.csv','rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
#    for row in spamreader:
#        n.append(row);
#k=0

#for i in range(0, len(n)):
#    for k in n[i]:
#        n2.append(float(k))
 
#print n2
def i2():
    z = []
    i2 = []

    with open('Book4.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|') 
        for row in spamreader:
            z.append(row);

    for i in range(0, len(z)):
        for m in z[i]:
            i2.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i2[i+1]-i2[i])
    return a
#n=[]
#n3=[]

#with open('Normal/n1.csv','rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
#    for row in spamreader:
#        n.append(row);

#for i in range(0, len(n1)):
#    for m in n[i]:
#        n3.append(float(m))

#print n3

#print i2

def i3():
    z=[]
    i3=[]

    with open('insomniac/i1.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i3.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i3[i+1]-i3[i])
    return a

def i4():    
    z=[]
    i4=[]
    with open('insomniac/i2.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i4.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i4[i+1]-i4[i])
    return a

def i5():
    z=[]
    i5=[]

    with open('insomniac/i3.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i5.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i5[i+1]-i5[i])
    return a

def i6():    
    z=[]
    i6=[]

    with open('insomniac/i4.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i6.append(float(m))

    a=[]
    for i in range(0, 1801):
        a.append(i6[i+1]-i6[i])
    return a

def i7():
    z=[]
    i7=[]

    with open('insomniac/i5.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i7.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i7[i+1]-i7[i])
    return a

def i8():
    z=[]
    i8=[]

    with open('insomniac/i6.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i8.append(float(m))

    a=[]
    for i in range(0, 1801):
        a.append(i8[i+1]-i8[i])
    return a

def i9():
    z=[]
    i9=[]

    with open('insomniac/i7.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i9.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i9[i+1]-i9[i])

    return a

def i10():
    z=[]
    i10=[]

    with open('insomniac/i8.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i10.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i10[i+1]-i10[i])
    return a

def i11():
    z=[]
    i11=[]

    with open('insomniac/i9.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i11.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i11[i+1]-i11[i])
    return a

def i12():
    z=[]
    i12=[]

    with open('insomniac/i10.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i12.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i12[i+1]-i12[i])
    return a

def i13():
    z=[]
    i13=[]

    with open('insomniac/i12.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i13.append(float(m))

    a=[]
    for i in range(0, 1801):
        a.append(i13[i+1]-i13[i])
    return a

def i14():
    z=[]
    i14=[]

    with open('insomniac/i13.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i14.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i14[i+1]-i14[i])
    return a

def i15():
    z=[]
    i15=[]

    with open('insomniac/i14.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i15.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i15[i+1]-i15[i])
    return a

def i16():
    z=[]
    i16=[]

    with open('insomniac/i15.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i16.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i16[i+1]-i16[i])
    return a

def i17():
    z=[]
    i17=[]

    with open('insomniac/i16.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i17.append(float(m))

    a=[]
    for i in range(0, 1801):
        a.append(i17[i+1]-i17[i])
    return a

def i18():
    z=[]
    i18=[]

    with open('insomniac/i17.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i18.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i18[i+1]-i18[i])
    return a

def i19():
    z=[]
    i19=[]

    with open('insomniac/i18.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i19.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i19[i+1]-i19[i])
    return a

def i20():
    z=[]
    i20=[]

    with open('insomniac/i19.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);
    for i in range(0, len(n1)):
        for m in z[i]:
            i20.append(float(m))
    
    a=[]
    for i in range(0, 1801):
        a.append(i20[i+1]-i20[i])

    return a

def i21():
    z=[]
    i21=[]

    with open('insomniac/i20.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i21.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i21[i+1]-i21[i])
    return a

def i22():
    z=[]
    i22=[]

    with open('insomniac/i21.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);


    for i in range(0, len(n1)):
        for m in z[i]:
            i22.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i22[i+1]-i22[i])
    return a

def i23():
    z=[]
    i23=[]
    with open('insomniac/i22.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in spamreader:
            z.append(row);

    for i in range(0, len(n1)):
        for m in z[i]:
            i23.append(float(m))
    a=[]
    for i in range(0, 1801):
        a.append(i23[i+1]-i23[i])
    return a

#    a = []
#b = []
#c = []
#d = []
#e = []
#f = []
	
#for i in range(0, (len(n1)-1)):
#    a.append(n1[i+1]-n1[i])
    #b.append(i1[i+1]-i1[i])
    #c.append(n2[i+1]-n2[i])
   # d.append(i2[i+1]-i2[i])
    #e.append(n3[i+1]-n3[i])
    #f.append(i3[i+1]-i3[i])







#s=0
#for i in range(0, (len(n1-1))):
#s2=sum(b)

#print b

#s=s/1802

#print s
#print a
#print b
#print c
#print d
#b.append(0.0)
#d.append(0.0)

#print f

#X = np.array([d,e,f])
#Y = np.array([2,1,2])

#clf = GaussianNB()
#clf.fit(X,Y)
#print clf.predict([c,b])                                
