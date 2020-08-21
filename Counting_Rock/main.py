def counting_rock():
    
   num_rocks = int(input("Enter the number of rocks present : - "))
   num_labaratory = int(input("Enter the number of laboratories : - "))
   count = 0
   final_count = []
   rock_sample = []
   for k in range(num_rocks):
       
       rock_size = int(input("Enter the size of samples"))
       rock_sample.append(rock_size)

   for i in range(num_labaratory):
       lab1,lab2 = (input().split())
   
       for element in range(len(rock_sample)):
           result = rock_sample[element]
           if(result in range(int(lab1),int(lab2))):
              count += 1
        
       final_count.append(count)
       count = 0
       
       
       for k in range(0, len(final_count)):
           
           output = final_count[k]
           
       print(output)
           

          
          
  
   
   
counting_rock()

