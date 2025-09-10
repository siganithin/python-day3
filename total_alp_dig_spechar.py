#program to find total number of alphabets , digits or special character in a string
def totalcount(str):
    alpha=0
    digits=0
    spechar=0
    for i in str:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digits += 1
        else:
            spechar += 1
    return alpha,digits,spechar
string=input("Enter the string:")
print("Total nuber of alphabets,digits and special characters are:",totalcount(string))