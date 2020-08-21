def minimum_gifts():
    
    gift_count = []
    check_rank = 0
    no_testcase = int(input("Enter the number of testcases :- "))
    for i in range(no_testcase):
        
        employee_rank = list(input("Enter the ranks of employee's :- "))
        for rank in range(len(employee_rank)):
            
            
            gift = int(employee_rank[rank])
            
            if(gift == 0):
                check_rank +=1
            
            elif(gift == 1):
               gift_count.append(1)
                
            elif(gift in range(2,6)):
                gift_count.append(2)
                
            else:
                print("Input error")
                
        if(check_rank == 0):     
            print("The total gift's to be distributed by the company are "+ str(sum(gift_count))+" "+ "in total")
        
        else:
            print("rank error since every employee should get a gift")
minimum_gifts()