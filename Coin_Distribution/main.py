from itertools import combinations

def distribute():
    
    num_children = int(input("Enter the number of children : -"))
    coin_values = [1,2,3,2,2,2,3]
    #coin_values = [5,3,10,1,2] #uncomment chesi check for other condition
    final_combo_value = []
    result = sum(coin_values)
    equal = int(result / num_children)
    print("Amount to be distributed to each child : -" + str(equal))
    output = set(list(combinations(coin_values,3)))
    print("The 3 coin combination")
    for index in output:
        
        if(sum(index) == equal):
            print(index)
            final_combo_value.append(index)
                
        else:
            continue
    print("The 2 coin combination ")    
    two_combo = set(list(combinations(coin_values,2)))
    for element in two_combo:
                
        if(sum(element) == equal):
            print(element)
            final_combo_value.append(element)
                    
        else:
            continue
    if(num_children == len(final_combo_value)):
       print("Possible set of coin to be distributed to children so they get equal share is :-")            
       print(final_combo_value)
       
    else:
        print("There is no combination such that each child gets a equal share")
    
distribute()
    
