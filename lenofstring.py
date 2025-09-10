def strlen(str):
    cnt=0
    for i in str:
        cnt += 1
    return cnt
string=input("Enter the string:")
print("length of string:",strlen(string))