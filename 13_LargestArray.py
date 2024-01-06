# l = [int(i) for i in input("Enter ").split(",")]

# print(l)


n=int(input("\n\nEnter how many no. u want to check : "))
l = []

for i in range(0,n):
    a=int(input(f"Enter the {i+1} no. : "))
    l.append(a)
    
max=0
    
for i in range(0,n):
    if(l[i]>max):
        max=l[i]
        
        
print(max)
