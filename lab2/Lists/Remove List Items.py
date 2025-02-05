#ex1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#ex2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#ex3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#ex4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#ex5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#ex6
thislist = ["apple", "banana", "cherry"]
del thislist
#ex7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)