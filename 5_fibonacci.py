

n=int(input("enter the no. :"))

a=0
b=1
series=0
print(a)
print(b)

for i in range(1,n-1,1):
    series=a+b
    a=b
    b=series
    print(series)