##import random
##passlen = int(input("enter the length of password:"))
##s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
##p = "".join(random.sample(s,passlen ))
##print (p)


##for i in range(5):
##    for j in range(6):
##        print('*',end='')
##     print()



##for i in range(5):
##    for j in range(i+1):
##        print('*',end='')
##    print()


##COMPREHENSION

##a=[41,23,25,90,52]
##t=[i+1 for i in a]
##print(t)

##a=[41,23,25,90]
##b=[(i,i+1) for i in a]
##print(b)

##a=[41,23,25,90]
##b=[(i,i*2) for i in a]
##print(b)

##a=[41,23,25,90,20,24,28,10,6,12]
##b=[i for i in a if i>10 and i%2==0]
##print(b)


##a=[i for i in range(0,101) if i%2==0]
##print(a)

##while True:
##    a = 0,1
##    print(a,end='')

##a=[i**2 for i in range(0,101,2)]
##print(a)

##b=[1,2,3,4,5]
###d={1:1,2:4,3:6,4:8,5:10}
##d={i:i*2 for i in b}
##print(d)


##a=['name','age']
##b=[['aryan','singhal','manaktala'],[22,21,23]]
##c=dict(zip(a,b))
##print(c)

##a=['name','age']
##b=[['aryan','singhal','manaktala'],[22,21,23]]
##c={a[i]:b[i] for i in range(0,2)}
##print(c)



