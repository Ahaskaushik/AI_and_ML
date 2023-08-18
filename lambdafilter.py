fib=[0,1,1,2,3,5,8,13,21,34]
oddf=[]
evenf=list(filter(lambda x: x if x%2==0 else oddf.append(x) , fib))
print("Even list = \n",evenf)
print("Odd list = \n",oddf)
print("\n")

#other method
fib=[0,1,1,2,3,5,8,13,21,34]
f=list(filter(lambda x:x%2!=0,fib))
print(f)

