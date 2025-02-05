#ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#ex2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#ex3
newlist = [x for x in fruits if x != "apple"]
#ex4
newlist = [x for x in fruits]
#ex5
newlist = [x for x in range(10)]
#ex6
newlist = [x for x in range(10) if x < 5]
#ex7
newlist = [x.upper() for x in fruits]
#ex8
newlist = ['hello' for x in fruits]
#ex9
newlist = [x if x != "banana" else "orange" for x in fruits]