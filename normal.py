import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB

def n1():
    n=[]
    n1=[]
    with open('Normal/n1.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n1.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n1[i+1]-n1[i])
    return a

def n2():

    n=[]
    n2=[]
    with open('Normal/n2.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n2.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n2[i+1]-n2[i])
    return a

def n3():

    n=[]
    n3=[]
    with open('Normal/n3.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n3.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n3[i+1]-n3[i])
    return a

def n4():

    n=[]
    n4=[]
    with open('Normal/n4.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n4.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n4[i+1]-n4[i])
    return a

def n5():

    n=[]
    n5=[]
    with open('Normal/n5.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n5.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n5[i+1]-n5[i])
    return a

def n6():

    n=[]
    n6=[]
    with open('Normal/n6.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n6.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n6[i+1]-n6[i])
    return a

def n7():

    n=[]
    n7=[]
    with open('Normal/n7.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n7.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n7[i+1]-n7[i])
    return a

def n8():
    n=[]
    n8=[]
    with open('Normal/n8.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n8.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n8[i+1]-n8[i])
    return a

def n9():

    n=[]
    n9=[]
    with open('Normal/n9.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n9.append(float(k))
    
    a=[]
    for i in range(0, 1801):
        a.append(n9[i+1]-n9[i])
    return a

def n10():
    n=[]
    n10=[]
    with open('Normal/n10.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n10.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n10[i+1]-n10[i])
    return a

def n11():
    n=[]
    n11=[]
    with open('Normal/n11.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n11.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n11[i+1]-n11[i])
    return a

def n12():
    n=[]
    n12=[]
    with open('Normal/n12.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n12.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n12[i+1]-n12[i])

    return a

def n13():
    n=[]
    n13=[]
    with open('Normal/n13.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
	    n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n13.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n13[i+1]-n13[i])
    return a

def n14():
    n=[]
    n14=[]
    with open('Normal/n14.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n14.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n14[i+1]-n14[i])
    return a

def n15():
    n=[]
    n15=[]

    with open('Normal/n15.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n15.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n15[i+1]-n15[i])
    return a

def n16():
    n=[]
    n16=[]

    with open('Normal/n16.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
	    n16.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n16[i+1]-n16[i])

    return a

def n17():
    n=[]
    n17=[]

    with open('Normal/n17.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n17.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n17[i+1]-n17[i])

    return a

def n18():
    n=[]
    n18=[]

    with open('Normal/n18.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n18.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n18[i+1]-n18[i])
    return a

def n19():
    n=[]
    n19=[]
    with open('Normal/n19.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n19.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n19[i+1]-n19[i])
    return a

def n20():
    n=[]
    n20=[]
    with open('Normal/n20.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n20.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n20[i+1]-n20[i])
    return a

def n21():
    n=[]
    n21=[]
    with open('Normal/n21.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n21.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n21[i+1]-n21[i])
    return a

def n22():
    n=[]
    n22=[]
    with open('Normal/n22.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n22.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n22[i+1]-n22[i])
    return a

def n23():
    n=[]
    n23=[]
    with open('Normal/n23.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n23.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n23[i+1]-n23[i])
    return a

def n24():
    n=[]
    n24=[]
    with open('Normal/n24.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n24.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n24[i+1]-n24[i])
    return a

def n25():
    n=[]
    n25=[]
    with open('Normal/n25.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row)

    for i in range(0, 1802):
        for k in n[i]:
	    n25.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n25[i+1]-n25[i])
    return a

def n26():
    n=[]
    n26=[]
    with open('Normal/n26.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n26.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n26[i+1]-n26[i])    
    return a

def n27():
    n=[]
    n27=[]
    with open('Normal/n27.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n27.append(float(k))

    a=[]
    for i in range(0, 1801):
        a.append(n27[i+1]-n27[i])
    return a

def n28():
    n=[]
    n28=[]
    with open('Normal/n28.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n28.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n28[i+1]-n28[i])
    return a

def n29():
    n=[]
    n29=[]
    with open('Normal/n29.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n29.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n29[i+1]-n29[i])
    return a

def n30():
    n=[]
    n30=[]
    with open('Normal/n30.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n30.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n30[i+1]-n30[i])
    return a

def n31():
    n=[]
    n31=[]
    with open('Normal/n31.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n31.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n31[i+1]-n31[i])
    return a

def n32():
    n=[]
    n32=[]
    with open('Normal/n32.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n32.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n32[i+1]-n32[i])
    return a

def n33():
    n=[]
    n33=[]
    with open('Normal/n33.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n33.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n33[i+1]-n33[i])
    return a

def n34():
    n=[]
    n34=[]
    with open('Normal/n34.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n34.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n34[i+1]-n34[i])
    return a

def n35():
    n=[]
    n35=[]
    with open('Normal/n35.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n35.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n35[i+1]-n35[i])
    return a

def n36():
    n=[]
    n36=[]
    with open('Normal/n36.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n36.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n36[i+1]-n36[i])
    return a

def n37():
    n=[]
    n37=[]
    with open('Normal/n37.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n37.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n37[i+1]-n37[i])
    return a

def n38():
    n=[]
    n38=[]
    with open('Normal/n38.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n38.append(float(k))
    return n38

def n39():
    n=[]
    n39=[]
    with open('Normal/n39.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n39.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n39[i+1]-n39[i])
    return a

def n40():
    n=[]
    n40=[]
    with open('Normal/n40.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n40.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n40[i+1]-n40[i])
    return a

def n41():
    n=[]
    n41=[]
    with open('Normal/n41.csv','rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            n.append(row);

    for i in range(0, 1802):
        for k in n[i]:
            n41.append(float(k))
    a=[]
    for i in range(0, 1801):
        a.append(n41[i+1]-n41[i])
    return a
