def noofwords(str):
    wordscount=str.split()
    return len(wordscount)
string=input("Enter the string:")
print("Total no.of words are:",noofwords(string))