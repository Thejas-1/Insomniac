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

m=mode([1,2,3,2,2,2,4])
print mode
