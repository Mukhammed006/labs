thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

#example1
for x in thisdict:
  print(x)

#example2
for x in thisdict:
  print(thisdict[x])

#example3
for x in thisdict.values():
  print(x)

#example4
for x in thisdict.keys():
  print(x)

#example5
for x, y in thisdict.items():
  print(x, y)