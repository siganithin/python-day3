# Write a Program to count occurrences of a character in given string.
 
# input: aaabbca
# output: a4b2c1
 

def prog(s):
    freq={}
    result=""
    for item in s:
        if item not in freq:
            count=0
            for x in s:
                if x==item:
                    count += 1
            freq[item]=count
            result += item + str(count)
    return result
string=input("Enter the string:")
res=prog(string)
print(res)