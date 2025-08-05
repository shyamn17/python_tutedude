a=int(input('Enter a number:'))

def factorial(a):
    f=1
    while a > 0:
        f*=a
        a-=1
    return f

r=factorial(a)
print('Factorial of',a ,'is:', r)
