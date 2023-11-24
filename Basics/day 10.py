##heights=[100,200,1000,300,5000]
##
##max_h=max(heights)
##print(max_h)


##############################
######AN0NYMOUS FUNCTION######
##############################
##SIMPLE 
##def multi(a):
##    return a*3
##print(multi(5))

##USING LAMBDA##
##t= lambda a: 'EVEN' if a%2==0 else 'ODD'
##print(t(4))

##USING MAP##
##l=[12,8,10,14]
##d=map(lambda a: a*2,l)
##print(list(d))

##l=[12,8,10,14]
##def myfun(n):
##    return n**n
##c=map(myfun ,l )
##print(list(c))
##print(tuple(c))

##l=[12,8,10,14]
##def myfun(n):
##    return n>10
##c=map(myfun ,l )
##print(list(c))
##print(tuple(c))


##USING FILTER##
##l=[45,8,10,14,15]
##a=filter(lambda x : x>10,l)
##print(list(a))

##USING MAP##
##l=[45,8,10,14,15]
##a=map(lambda x : x>10,l)
##print(list(a))


##l=[45,8,10,14,15]
##a=map(lambda x: x>15,l)
##b=filter(lambda x: x>15,l)
##print(list(a))
##print(list(b))

##import mymod
##print(mymod.abc())
