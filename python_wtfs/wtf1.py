"""
Python WTFs: Mutable function arguments
"""

"""
Problem 1:
    Read the definition of the function `integer_parameter`. Without calling the
    function, suppose you define a list variable and call the function with it
    as the argument. Predict what you think the function will do.
"""


def integer_parameter(integer):
    integer += 1
    return integer


"""
Problem 2:
    Uncomment the three statements below and run the file. Does the function do
    what you expected? Specifically, is the variable `my_var` what you expected
    it would be after calling the function?
"""

# my_var = 2
# print(integer_parameter(my_var))
# print(my_var)


"""
Problem 3:
    Read the definition of the function `list_parameter`. Without calling the
    function, suppose you define a list variable and call the function with it
    as the argument. Predict what you think the function will do.
"""


def list_parameter(lst):
    lst += [1]
    return lst


"""
Problem 4:
    Uncomment the two statements below and run the file. Does the function do
    what you expected?
"""

# my_var = [0]
# print(list_parameter(my_var))

"""
Problem 5:
    Recomment the above two statements. Without calling the function again,
    predict what you think the variable `my_var` is now. Then, uncomment the
    three statements below and run the file. Is `my_var` what you expected it
    would be after calling `list_parameter`?
"""

# my_var = [0]
# print(list_parameter(my_var))
# print(my_var)

"""
WTF??? Why did that happen?
    The answer is that integers are immutable objects and lists are mutable
    objects. Immutable objects are ones that CAN'T be modified (or mutated)
    after they're created and mutable objects are ones that CAN be modified (or
    mutated) after they're created. So, whenever the function is called with a
    mutable object argument, it updates the variable that's passed to the
    function; it doesn't created a new one.

    What happens with immutable objects? Well, since you can't modify immutable
    objects, whenever you "change" an immutable object, you're actually creating
    a new object that has the value of the "changed" original object; this
    leaves the original object unchanged.
"""

"""
What to do instead?
    It really depends on what you're trying to do. If you don't want to modify
    an object that's passed to a function, you can create a deep copy of the
    original object:

```
import copy


def list_parameter(lst):
    new_lst = copy.deepcopy(lst)
    new_lst += [1]
    return new_lst
```

    That's a somewhat extreme way to get around this behavior, and what you
    should do will likely change based on what you want your code to do. This is
    just something important to keep in mind.
"""
