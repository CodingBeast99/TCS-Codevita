def minimize_sum():
    
    size = int(input("Enter the size of the list : "))
    operations = int(input("Enter no of operations : "))
    array_list = []
    count = 0
    for i in range(size):
        
        user_input = int(input())
        array_list.append(user_input)
        
    
    for j in range(operations):
        result = array_list[count]
        operations_value = int(result/2)
        array_list.remove(result)
        array_list.append(operations_value)
        array_list.sort(reverse = True)
        print(array_list)
        
            
 
    
    print("Final output after operations "+ str(array_list))
    print("Thier minimize sum is "+str(sum(array_list)))
minimize_sum()