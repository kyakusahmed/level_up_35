
file = open('VIP.txt','r')


file1 = open('Ord.txt','r')

 
ORD = []
VIP = []

for line in file:
    VIP.append(line)
for line in file1:
    ORD.append(line)



def name_checker(name,data):
    result = None
    for fullname in data:
        if fullname.casefold().find(name.casefold()) != -1:
            result = fullname
    
    
    return result
    
while True:
    name1 = input('enter guest name! ')

    if name_checker(name1,VIP) == None:
        if name_checker(name1,ORD) == None:
            print ("Not Registered")
        else:
            print(name_checker(name1,ORD))
    
    else:
        print(name_checker(name1,VIP))

