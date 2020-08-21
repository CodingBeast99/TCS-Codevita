def largest_factor():
    
    user_choice = int(input("Enter a number : "))
    large_factor = int(input("Enter the k value to get the kth largest factor : "))
    num = user_choice
    num_list = []
    factor_list = []
    count = 0
    divisor_list = []
    for i in range(1,(num+1)):
        num_list.append(i)
        
    for j in range(len(num_list)):
        if(user_choice % num_list[j] == 0 ):
            #print("Available divisor's are "+ str(num_list[j]))
            divisor_list.append(num_list[j])
            
        
    print("Divisor's for " + str(user_choice)+ str(divisor_list))
    
    for element in range(len(divisor_list)):
        output = divisor_list[element]
        factor_list = []
        for index in range(len(num_list)):
            if(output % num_list[index] == 0):
                factor_list.append(num_list[index])
                
        
        if(len(factor_list) == large_factor):
            print("The k'th largest divisor is " + str(output))
            
        
        
largest_factor()