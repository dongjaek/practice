"""
Q. How are python objects create/update/delete lifetimes reflected in their references?

A.
We start out with one object with one memory address under the hood.
We assign many variables to this object, hence we have multiple references to the same object

Once changed, the old references need not move because the object still has references tied to it
A new object and reference is generated and l1 is tied to it. Hence we are binding to the object 
reference not to the pointer reference.

In other words, the language implements reference counting and object creation, duplication, w/e
is conducted lazily.

Furthermore we know that state is not changed if there are references remaining to it, instead a new
object is created for the new state assuming the previous state still had references.
"""

l1 = [1,2,3,4,5]
l2 = l1
l3 = l1
print id(l1)
print id(l2)
print id(l3)

print l1
print l2
print l3

l1 = 42

print l1
print l2
print l3

print id(l1)
print id(l2)
print id(l3)
