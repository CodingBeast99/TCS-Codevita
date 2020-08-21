def divine_divisor():
    
   
    num = 20
    num_list = []
    user_choice = int(input())
    for i in range(1,(num+1)):
        num_list.append(i)
        if(user_choice % i == 0):
            print("Available divisors are "+ str(i))
            
        else:
            continue
        
divine_divisor()
       
    
    