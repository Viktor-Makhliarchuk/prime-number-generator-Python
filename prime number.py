import math 
import os
file_name = "prime_numbers.txt"
def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1 ):
        if num % i == 0:
            return False
    return True
    

end_string = ""
if os.path.exists(file_name):
    file = open(file_name , "r")
    for string_temp in file:
        end_string = string_temp
        temp = end_string
    file.close()
    file = open(file_name , "a")
else:
    file = open(file_name , "w")
             
            
if end_string != "":
    num = int(end_string) + 1
else:
    num = 3
print("start " + str(num))   
k=0
tys = 0
while True:
    if is_prime(num):
        file.write(str(num)+ "\n")
        k += 1

        if k > 10000:
            file.close()
            file = open(file_name , "a")
            tys += 1
            print(str(tys) + "0000 szt")
            k=0
   
    num += 1
    
     
