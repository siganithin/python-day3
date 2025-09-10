def totalduplicates(lst):
    dup = 0
    for i in range(len(lst)):
        cnt = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                cnt += 1
        if cnt > 1:
            dup += 1
    return dup
my_list=[12,22,12,33,43,13,4,5,2,42,2,4]
res=totalduplicates(my_list)
print("Total number of duplicate numbers are:",res)
            
