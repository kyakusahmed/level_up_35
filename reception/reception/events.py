file = open('VIP.txt','r')


file1 = open('Ord.txt','r')


ORD = []
VIP = []

for line in file:
    VIP.append(line)
for line in file1:
    ORD.append(line)



def register_check(name,data):
    result = False
    for fullname in data:
        if fullname.casefold().find(name.casefold()) != -1:nhg
            result = fullname

    return result 

while True:
    name1 = input("enter your name! ")
       
    print(register_check(name1,VIP))





        


    