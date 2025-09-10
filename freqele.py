#count frequency of each element in list.
def freqele(lst):
    freq={}
    for item in lst:
        if item not in freq:
            count=0
            for x in lst:
                if x==item:
                    count += 1
            freq[item]=count
    return freq
my_list=[12,34,12,45,43,53,1,2,3,2]
res=freqele(my_list)
print(res)


