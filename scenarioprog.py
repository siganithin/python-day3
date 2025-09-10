# A 3-day tech workshop collected attendee registrations separately for each day. 
# You are given three lists (day1, day2, day3) of 
# email addresses — lists may contain duplicates (people registering multiple times) and 
# email case may vary (Upper/Lower).

# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.

n1=int(input("Total no.of people attended on day1:"))
lst1=[]
for i in range(n1):
    mails=input(f"Enter mail of student{i+1}:")
    lst1.append(mails)
print(lst1)
print("total mails recieved:",lst1)
n2=int(input("Total no.of people attended on day2:"))
lst2=[]
for i in range(n2):
    mails=input(f"Enter mail of student{i+1}:")
    lst2.append(mails)
print("total mails recieved:",lst2)
n3=int(input("Total no.of people attended on day3:"))
lst3=[]
for i in range(n3):
    mails=input(f"Enter mail of student{i+1}:")
    lst3.append(mails)
print("total mails recieved:",lst3)

def cleandays(lst1,lst2,lst3):
    #1.Cleans each day's list (normalizes case, removes duplicates).
    s1=set(lst1)
    s2=set(lst2)
    s3=set(lst3)
    print(f"on day1:{s1}\n on day2:{s2} \n on day3:{s3}")
cleandays(lst1,lst2,lst3)
#Prints the total number of unique attendees across all days.

