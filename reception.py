file = open('VIP.txt','r')

file1 = open('Ord.txt','r')

 
ORD = []
VIP = []
for line in file:
    VIP.append(line)
for line in file1:
    ORD.append(line)



def registration_checker(name,data):
    result = "User Not Registered"
    for fullname in data:
        
        if fullname.casefold().find(name.casefold()) != -1:
            result = fullname
            return result 
        
        
    
    return result
 
 
 
 
 
while True:
    name1 = input("enter your name! ")
       
    print(registration_checker(name1,VIP))


    

    print(registration_checker(name1,ORD))
