# n = int(input("Enter the number"))

# flag = 0
# for i in range (2 , int(n/2)+1 , 1):
#     if(n % i == 0):
#         flag += 1
#         break

# if(flag == 0):
#     print("prime")
# else:
#     print("Not prime")n


n=int(input("enter the no. : "))

for i in range(2,int(n/2)+1,1):
    if(n%i==0):
        print("not prime")
        break
    else:
        print("prime")

