def compare(str1,str2):
            if str1==str2:
                print("Two strings are same")
            else:
                print("Two strings are not same")
def concat(str1,str2):
    return str1+str2
st1=input("Enter string 1:")
st2=input("Enter string 2:")
compare(st1,st2)
print("Concate of two strings:",concat(st1,st2))
