mylist=["apple", "banana", "cherry"]
#print(mylist[0:3])
#if "apple" in mylist:
    #print("Yes, 'apple' is in the fruits list")
#mylist[1]="mango"
#print(mylist)
mylist.append("orange")
print(mylist)
mylist.insert(1,"grapes")
print(mylist)
thislist=["x", "y"]
mylist.extend(thislist)
print(mylist)
mylist.remove("x")
print(mylist)
mylist.pop(-1)
print(mylist)