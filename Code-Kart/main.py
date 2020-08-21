def codekart():

    print("****************** Welcome to CODE KART ******************")
    
    operation_size = int(input("Enter the number of operations to be performed : "))
    inventory = [] 
    count = 0
    
    for num_operations in range(operation_size):
        
        user_choice = input("Enter command to perform operations : ")
        
        if(user_choice == "ADD"):
            item = input("Enter the item name : ")
            qauntity = int(input("Enter the qauntity : "))
            for item_name in range(qauntity):
               inventory.append(item)
               count += 1
        
        
            if(count > 0):
               print("Sucessful item has been added with code 1")
             
            else:
            
               print("Error adding item to inventory with code -1")
        
        
        elif(user_choice == "REMOVE"):
              item_removal = input("Enter the item name which has to be removed : ")
              item_quantity = int(input("Enter the quantity of item : "))
              
              try:
                 for x in range(item_quantity):
                     if(item_removal in inventory):
                         print("ITEM exists")
                         inventory.remove(item_removal)
                         count += 1
                         print("Inventory update after operation has been performed " +str(inventory))
                         
            
              except Exception as ex:
                     print(ex)
        
        elif(user_choice == "MY_CART"):
             if(len(inventory) == 0):
                 print("You have no items in your inventory")
                 print("To get quantity of each item in inventory choose suitable command")
             
             else:
                  print(inventory)
                  print("You have "+str(len(inventory)) + " "+"items")
    
    
        elif(user_choice == "GET_QUANTITY"):
             user_input= input("Enter the item name of item : ")
             print("You have "+ str(user_input) + "*" + str(inventory.count(user_input)))
    
    
        elif(user_choice == "CHECKOUT"):
            print("You have "+ str(len(inventory))+ " items")
            for each in range(len(inventory)):
                exp = 0
                counter = 0
                result = inventory[each]
                if(result == "shoe"):
                    cost = inventory.count(result)
                    counter += cost
                    
        
                elif(result == "shirt"):
                    item_cost = inventory.count(result)
                    exp += item_cost
                    
            if(counter > 0):     
                print("You have to pay an amount of "+ str(counter * 50)+ "$")
                
            else:
                break;
                print("You have o items in inventory")
            
            if(exp > 0):
                print("You have to pay an amount of "+ str(exp * 150) + "$")
                
                
            else:
                break;
                print("You have 0 items in inventory")
                
                
        elif(user_choice == "quit()"):
            print("Thanking for shopping with us ")
            break;
            
        
        else:
            print("Command not found error")
            break;
            
    
codekart()
    

