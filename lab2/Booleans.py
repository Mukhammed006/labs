#Example1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example3
print(bool("Hello"))
print(bool(15))

#Example4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Example5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Example6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Example7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Example8
def myFunction() :
  return True

print(myFunction())

#Example9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Example10
x = 200
print(isinstance(x, int))

#ex1
print(10 > 9)
#output: True

#ex2
print(10 == 9)
#output: False

#ex3
print(10 < 9)
#output: False

#ex4
print(bool("abc"))
#output: True

#ex5
print(bool(0))
