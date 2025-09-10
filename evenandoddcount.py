def evenoodcnt(lst):
    evencnt=0
    oddcnt=0
    for i in lst:
        if i%2==0:
            evencnt += 1
        else:
            oddcnt += 1
    return evencnt,oddcnt
n=int(input("enter size:"))
lst=[]
for i in range(n):
    e=int(input("Element:"))
    lst.append(e)
res=evenoodcnt(lst)
print(res)
