n=int(input("Enter the no. : "))

# count=0


for i in range (2,n+1,1):

    count=0
    for j in range (2,int(i/2),1):
        if (i%j==0):
          count += 1
          break
    if(count == 0):
      print(i)

