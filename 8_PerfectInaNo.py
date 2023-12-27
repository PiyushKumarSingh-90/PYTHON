n=int(input("enter no. : "))

for i in range(1,n+1,1):
    z=0
    for j in range(1,i,1):
        if(i%j==0):
          z+=j

    if(z==i):  
      print(i)         






