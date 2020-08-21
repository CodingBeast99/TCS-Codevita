from itertools import combinations as cbm

def seating():
    
    table_count = int(input())
    num_attendes = int(input())
    total_combo = table_count * num_attendes
    print("Checking the 3 combo")
    result = list(cbm(range(1,num_attendes+1),3))
    print("checking the 2 combo")
    output = list(cbm(range(1,num_attendes+1),2))
    final_list = result + output
    if(len(result) == total_combo):
    
        print(final_list)
        
    else:
        print("error combo not possible")
        

seating()
            