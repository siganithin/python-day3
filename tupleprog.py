def studdetails(t):
    print("Student Details Tuple:", t)
tup = () 
for i in range(2):
    ele = input(f"Enter detail {i+1}: ")
    temp_list = list(tup)   
    temp_list.append(ele)    
    tup = tuple(temp_list)  
studdetails(tup)
