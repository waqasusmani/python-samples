x = lambda a,b,c : a+b+c
print("From lambda function -->> ",x(2,5,8))

def addThreeNumbers(a,b,c):
    return a+b+c
print("Three numbers added -->> ",addThreeNumbers(5,8,10))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))