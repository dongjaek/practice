"""
Q. What is an abstract base class in Python?

A. 
ABC (PEP 3119) is Python's way of enforcing at compile time the implementation
of methods in an inheritance hierarchy.

Statically typed languages which enforce strong compile time behaviours have
the 'interface' which allows programmers to extract design from implementation
in a hierarchical fashion.

Python does not have these behaviours by default and most classes tend to be
very tightly coupled and stateful as a result.

The way around this is to write an class in Python with an abc decorator
making this the functional equivalent of a Python interface and then to 
implement functionality in an inheriting child class

This is still more work than traditional statically type languages
because we have to apply the decorator and check things in children,
but with the python model, it's the best we can do.

https://dbader.org/blog/abstract-base-classes-in-python
https://docs.python.org/2/library/abc.html
"""

from abc import ABC, abstractmethod, ABCMeta

class AbstractClassExample(ABC):

  @abstractmethod
  def a(self):
    raise NotImplementedError()



"""
Example. Stack interface with many implementations
"""
