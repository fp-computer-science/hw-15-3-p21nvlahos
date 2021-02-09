# Author NV: 2/6/2021

#Question 1
library = {"Harry Potter":"J.K Rowling", "The Lord of the Rings":"J.R.R Tolkien", "The Hunger Games":"Suzanne Collins", "The Chronicles of Narnia":"C.S. Lewis"}

#Question 2
print(library.values())

#Question 3
print(library.keys())

#Question 4
print("Harry Potter" in library)

#Question 5
print("Star Wars" not in library)

#Question 6
library["Green Eggs and Ham"] = "Dr. Suess"
print(library)

#Question 7
print(len(library))

#Question 8
print(library["The Chronicles of Narnia"])

#Question 9

print(library.items())

#Question 10
del(library["The Lord of the Rings"])