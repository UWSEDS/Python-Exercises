"""
Python WTFs: Empty mutable default function arguments
"""

"""
Problem 1:
    Read the definition of the function `empty_list_parameter`. Without calling
    the function, predict what you think the function will do when it's run
    once.
"""


def empty_list_parameter(lst=[]):
    lst += [1]
    return lst


"""
Problem 2:
    Uncomment the statement below and run the file. Does the function do what
    you expected?
"""

# print(empty_list_parameter())

"""
Problem 3:
    Recomment the above line. Without calling the function again, predict what
    you think the function will do when the function is run multiple times.
    Then, uncomment the for loop below and run the file. Does the function do
    what you expected it would when it's called 4 times?
"""

# for i in range(4):
#     print(empty_list_parameter())

"""
Why does this happen?:
    The simple reason is that the function uses the same list object every time
    it's called. In other words, when the function is defined, it creates a new
    list object for the default parameter. Then, whenever the function is
    called, it always uses that same list object. Since the object is mutable,
    it gets updated every time the function is called. The important thing to
    note is that calling the function DOES NOT create a new object every time
    the function is called. A single mutable object is created when the function
    is defined and is used every time.

    You can think of `empty_list_parameter` being equivalent to the following:

```
empty_list_parameter_2_arg = []

def empty_list_parameter_2(lst=empty_list_parameter_2_arg):
    lst += [1]
    return lst
```

What to do instead?:
    To avoid this, don't use mutable objects for default function parameters!
    Instead, use `None` as the default value and create a new object within the
    function body:

```
def empty_list_parameter_fixed(lst=None):
    if lst is None:
        lst = []
    lst += [1]
    return lst
```
"""
