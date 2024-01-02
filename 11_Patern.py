n=int(input("enter the no. of row : "))


# RIGHT ANGLE TRIANGLE:-



# for i in range (1,n+1,1):
#     for j in range(i):
#         print(" * ",end=" ")
#     print(" ") 


# DIAMOND:-



# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")

#     print("")

# for i in range(n-1,0,-1):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for k in range(2*i-1): 
#         print("*",end="")

#     print("")



# HOLLOE DIAMOND:-



# for i in range(1,n+1):
#     for j in range(n+1,i,-1):
#        print("x",end="")
#     for k in range(2*i-1):
#         if k == 0 or k == 2*i-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
    
#     print("")
    
# for i in range(n-1,0,-1):
#     for j in range(n+1,i,-1):
#         print(" ",end="")
#     for k in range(2*i-1): 
#         if k == 0 or k == 2*i-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")





#       *         * 
#      * *       * * 
#     * * *     * * * 
#    * * * *   * * * * 
#   * * * * * * * * * *  





for i in range(1,n+1): 
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
            
    print("") 




# A B C D E 
#  B C D E 
#   C D E 


 
    
    
# n = 5
# char = 65
# for i in range(n - 2):
#     char = 65 + i
#     for s in range(i):
#         print(" ", end ="")
#     for j in range(n - i):
#         print(chr(char), end=" ")
#         char += 1
#     print()
   
    
     
    
    
#     C D E 
#    B C D E 
#   A B C D E 
#    B C D E 
#     C D E 
    
    
    
  
    
# n = 5
# char = 65

# for i in range(3, n+1):
#     char = 65 + n - i
#     for s in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print(chr(char), end=" ")
#         char+=1
#     print()

# for i in range(1,n - 2):
#     char = 65 + i
#     for s in range(i):
#         print(" ", end ="")
#     for j in range(n - i):
#         print(chr(char), end=" ")
#         char += 1
#     print()
        
    

   

