#example1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#example3
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#exmaple4
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#example5
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)