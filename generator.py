"""
Q. What is a python generator and how is it useful?

A generator is an higher level function implemented into the language through
syntactic sugar.

The are especially powerful when we need the following:
  O(1) storage space for a series of objects
  Dynamic object series manipulation (change how the series is generated)
  Clean code rather than a for loop
  We do not want to store values, we have a specific requirement of the next step only.

A generator is a function which has a code block which 'generates' the next item in the sequence

"""

"""
 Generator examples:
 range()
 fibonacci() : any numberic series from a closed-form solution
 list / string manipulation which is conducted serially

 Huge text file parsing (log parsing)
 - don't read things into a single list.

Don't throw large processing units to that which can be done cleanly and elegantly
"""

# Iterate over a loop

# List parsing

# Log processing

# Fibonacci
