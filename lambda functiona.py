# lamda functions square root 



list1=[4,5,6,7,8]
list2=list(map(lambda x: x**2 , list1))
print(list2)
m=[1,2,3,4]
print(m*2)



list1=[4,5,6,7,8]
list2=list(map(lambda x: x-2 , list1))
print(list2)
m=[1,2,3,4]
print(m*2)



from functools import *
list1=[1,2,3,4,5,6]
r=reduce(lambda x,y:x,list1)
p=reduce(lambda x,y:y,list1)
w=reduce(lambda x,y:x+y , list1)
z=reduce(lambda x,y:x-y , list1)
print(r)
print(p)
print(w)
print(z)





