def vowelandconsonents(str):
    vowels="aeiouAEIOU"
    vowelcount=0
    consonentcount=0
    for i in str:
        if i in vowels:
            vowelcount += 1
        else:
            consonentcount += 1
    return vowelcount,consonentcount
string=input("Enter the string:")
print("total no of vowels and consonents are:",vowelandconsonents(string))
    