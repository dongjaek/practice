"""
Q. In python, are we dealing with pass by reference or pass by value?

A.
Lazily instantiated object creation with pass-by-reference semantics.
An object is passed by reference and continues under the reference until
mutation of state is detected, in which case a new object is created
to encapsulate the new state as long as the old object still has references
attached to it.

This is why the GIL is the way it is.
"""

def change(x):
  print id(x)
  x += 10
  # x has become a new object y
  print id(x)
  return x


x = 10
print id(x)
y = change(x)
print id(x)
# x still has references attached to it from the exterior scope
# line 22: therefore still exists.
print x
# y has move semantics so instead of a copy we have the same reference returned
# to avoid any more memory allocation and copies
print id(y)
