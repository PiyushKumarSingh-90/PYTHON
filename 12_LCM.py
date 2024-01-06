n1=int(input("Enter the 1st no. : "))
n2=int(input("Enter the 2nd no. : "))

sum=1

for i in range(2,n1-1,1):
    if(n1%i==0 or n2%i==0):
        sum*=i
        
print("LCM of ",n1," & ",n2," is = ",sum)
        
    

