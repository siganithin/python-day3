def setprog(set):
    return set
n=int(input("Enter size of set:"))
s=set()
for i in range(n):
    ele=input("Enter elements:")
    s.add(ele)
res=setprog(s)
print(res)