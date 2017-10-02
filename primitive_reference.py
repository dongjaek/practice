"""
Q. Do primitives have a reference?

A.
Under the hood they are variables which are assigned this value. Hence they have references.
This is because there are no primitives in python, everything is an object, hence even 
traditional primitive types such as int, bool, string are actually objects under the hood
and therefore fall under the same restrictions and implementation details as other objects

In Python we do not have access to the pointers, as this would allow us to change the reference
counting behaviour and break the encapsulation of garbage collection through the references.
The CPython behaviour likely uses pointers under the hood but we can only really see and understand
the system at the level of a reference since we do have the ability to manipulate 
or pass the construct.
"""

print id(1)
print id(2)
print id(3)
