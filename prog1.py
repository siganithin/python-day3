def prog():
    # my_list=[]
    # my_list.append(1)
    # my_list.append(2)
    # print(my_list)
    n=int(input("Enter how many numbers in list:"))
    lst=[]
    for i in range(n):
        ele=input("enter element:")
        lst.append(ele)
    return lst
res=prog()
print(res)