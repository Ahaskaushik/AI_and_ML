from functools import reduce
lst=[10,1,2,3,5]
z=reduce(lambda x,y: x if (x>y) else y,lst)
print(z)
print("\n")


from functools import reduce
lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y:x+y,lst)
print(x)

