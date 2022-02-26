#How to declarate Static Typing in python

a: int = 5
b: str = 'Hello'
c: bool = True

print(a,b,c)



#In functions

def sum(a:int , b:int) -> int:
    return a + b

print(sum(1,2))