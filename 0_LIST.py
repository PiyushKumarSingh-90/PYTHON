#                               LIST FUNCTION KEYS


mylist=["apple","banana","cherry"]

# print(len(mylist))           # 1. How many items a list has, use the { len() } function:



# if "apple"  in mylist:       # 2.if a specified item is present in a list use the { in } keyword:
    # print("na")



# mylist.insert(1,"mango")     # 3. The { insert() } method inserts an item at the specified index:
# print(mylist)



# mylist.append("lechi")       # 4. To add an item to the end of the list, use the { append() } method:
# print(mylist)



# thislist=("lemon","bringl")  # 5. To append elements from another list to the current list, use the { extend() } method. 
# mylist.extend(thislist)
# print(mylist)



# mylist.remove("banana")      # 6. The { remove() } method removes the specified item.
# print(mylist)



# mylist.pop(1)                # 7. The pop() method removes the specified index.
# print(mylist)



# del mylist[0]                # 8. The del keyword also removes the specified index:
# print(mylist)



# newlist = [x.upper() for x in mylist]  
# print(newlist)               # 9. Set the values in the new list to upper case:



# mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# mylist.sort()           
# print(mylist)                 # 10. List objects have a { sort() } method that will sort the list alphanumerically, ascending, by default:



# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)                # 11. To sort descending, use the keyword argument { reverse = True }



# mylist = ["apple", "banana", "cherry"]
# thislist = mylist.copy()        
# print(thislist)                 # 12. Make a copy of a list with the { copy() } method



# mylist = ["apple", "banana", "cherry"]
# thislist = list(mylist)
# print(mylist)                     # 13. Another way to make a copy is to use the built-in method{ list() }



# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2             # 14. One of the easiest ways are by using the + operator.
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:                   # 15. Another way to join two lists is by appending all the items from list2 into list1, one by one
#     list1.append(x)

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)               # 16. Use the{ extend() }method to add list2 at the end of list1
# print(list1)


