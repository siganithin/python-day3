#print all unique elements in a list
def uniqueele(lst):
    for i in range(len(lst)):
        count=0
        for j in range(len(lst)):
            if lst[i]==lst[j]:
                count += 1
        if count==1:
            print(lst[i],end=" ")
my_list=[1,23,42,40,12,43,13,12,2,1]
print("unique elemnts are:",uniqueele(my_list))