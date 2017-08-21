import insomniac
import normal
from collections import Counter
import random
import matplotlib.pyplot as plt
n1=[]
n2=[]
n3=[]
n4=[]
n5=[]
n6=[]
n7=[]
n8=[]
n9=[]
n10=[]
n11=[]
n12=[]
n13=[]
n14=[]
n15=[]
n16=[]
n17=[]
n18=[]
n19=[]
n20=[]
n21=[]
n22=[]
n23=[]
n24=[]
n26=[]
n27=[]
n28=[]
n29=[]
n30=[]
n31=[]
n32=[]
n33=[]
n34=[]
n35=[]
n36=[]
n37=[]
n38=[]
n39=[]
n40=[]
n41=[]

n1=normal.n1()
n2=normal.n2()
n3=normal.n3()
n4=normal.n4()
n5=normal.n5()
n6=normal.n6()
n7=normal.n7()
n8=normal.n8()
n9=normal.n9()
n10=normal.n10()
n11=normal.n11()
n12=normal.n12()
n13=normal.n13()
n14=normal.n14()
n15=normal.n15()
n16=normal.n16()
n17=normal.n17()
n18=normal.n18()
n19=normal.n19()
n20=normal.n20()
n21=normal.n21()
n22=normal.n22()
n23=normal.n23()
n24=normal.n24()
n25=normal.n25()
n26=normal.n26()
n27=normal.n27()
n28=normal.n28()
n29=normal.n29()
n30=normal.n30()
n31=normal.n31()
n32=normal.n32()
n33=normal.n33()
n34=normal.n34()
n35=normal.n35()
n36=normal.n36()
n37=normal.n37()
n38=normal.n38()
n39=normal.n39()
n40=normal.n40()
n41=normal.n41()

i1=[]
i2=[]
i3=[]
i4=[]
i5=[]
i6=[]
i7=[]
i8=[]
i9=[]
i10=[]
i11=[]
i12=[]
i13=[]
i14=[]
i15=[]
i16=[]
i17=[]
i18=[]
i19=[]
i20=[]
i21=[]
i22=[]
i23=[]

i1=insomniac.i1()
i2=insomniac.i2()
i3=insomniac.i3()
i4=insomniac.i4()
i5=insomniac.i5()
i6=insomniac.i6()
i7=insomniac.i7()
i8=insomniac.i8()
i9=insomniac.i9()
i10=insomniac.i10()
i11=insomniac.i11()
i12=insomniac.i12()
i13=insomniac.i13()
i14=insomniac.i14()
i15=insomniac.i15()
i16=insomniac.i16()
i17=insomniac.i17()
i18=insomniac.i18()
i19=insomniac.i19()
i20=insomniac.i20()
i21=insomniac.i21()
i22=insomniac.i22()
i23=insomniac.i23()

#data=Counter(i23)
#data.most_common(1)

def mode(nums):
    corresponding={}
    occurances=[]
    for i in nums:
            count = nums.count(i)
            corresponding.update({i:count})

    for i in corresponding:
            freq=corresponding[i]
            occurances.append(freq)

    maxFreq=max(occurances)

    keys=corresponding.keys()
    values=corresponding.values()

    index_v = values.index(maxFreq)
    global mode
    mode = keys[index_v]
    return mode

m=mode(i2)
#print m
#n=mode(i1)

patients ={1:n1,2:n2,3:n3,4:n4,5:n5,6:n6,7:n7,8:n8,9:n9,10:n10,11:n11,12:n12,13:n13,14:n14,15:n15,16:n16,17:n17,18:n18,19:n19,20:n20,21:n21,22:n22,23:n23,24:n24,25:n25,26:n26,27:n27,28:n28,29:n29,30:n30,31:n31,32:n32,33:n33,34:n34,35:n35,36:n36,37:n37,38:n38,39:n39,40:n40,41:n41,42:i1,43:i2,44:i3,45:i4,46:i5,47:i6,48:i7,49:i8,50:i9,51:i10,52:i11,53:i12,54:i13,55:i14,56:i15,57:i16,58:i17,59:i18,60:i19,61:i20,62:i21,63:i22,64:i23}
#print i11
#print patients[52]
#i=[]
#i=patients[51]
#print i
#m=mode(i1)
#print m
k=random.sample(range(1,63),6)
#print k
data = Counter(i1)
print data.most_common(1)

for i in data.most_common(1):
    print i
for j in i:
    print j

#print patients[21]
x=[]
y=[]
def classify(args):
    del x[:]
    del y[:]
    for i in args:
#	del x[:]
#	del y[:]
        data=Counter(patients[i])
        j=data.most_common(1)
        for k1 in j:
	    x.append(k1[0])
	    y.append(k1[1])
    print x
    print y
    plt.plot(x, y, label='1')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title("Classification of selected samples")
    plt.show()
#            for k2 in k1:
	        			
#		if k2==0.0:
#                    print "insomniac [",i,"] is insomniac"
#		else:
# 		    print "normal[",i,"] is normal"  
    
for i in range(1,10):
    k=random.sample(range(1,63),6)
    classify(k)
    
