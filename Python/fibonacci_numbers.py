def fib(x):
    a=0
    b=1
    if x<=0:
        print("invalid")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            a=b
            b=c
            print(c)
x=int(input("Enter a number: "))
fib(x)
