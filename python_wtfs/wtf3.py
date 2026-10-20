"""
Python WTFs: Comparing to `None`
"""

"""
Problem 1:
    Python style guides will often say something like this:
        "Don't compare to`None` with `x == None`. Use `x is None` instead."
    Why is that the case? Shouldn't `==` and `is` be the same? Uncomment the
    two statements below. Do the two statements evaluate equivalently?
"""

# print(None == None)
# print(None is None)

"""
Problem 2:
    Recomment the two statements above and uncomment the two statements below.
    Do the two statements evaluate equivalently?
"""

# print(str("hi!") == None)
# print(str("hi!") is None)

"""
Problem 3:
    Recomment the two statements above and uncomment the four statements below.
    Now do the statements evaluate equivalently?
"""

# from wtf3_lib import Foo
# foo = Foo()
# print(foo == None)
# print(foo is None)


"""
WTF??? Why did that happen?
    To see why that happened, look at the file `wtf_lib.py`. In it, we have the
    definition of the `Foo` class. This class has a method `__eq__` which is a
    special method that's invoked whenever Python's `==` operator is used to
    compare two objects. In other words, whenever you do `foo() == x`, Python
    calls `foo().__eq__(x)`, which always returns `True`!

    The general takeaway here is that, in Python, classes can redefine the
    equality operator to have custom behavior. This is actually something that
    comes up in one of the most frequently used Python libraries, numpy, which
    we'll use later in this class.

    Unlike the equality operator, however, the keyword `is` in Python has a very
    specific meaning and classes can't redefine how `is` works.
"""

"""
What to do instead?
    This one's easy: just listen to the style guides! You should never compare
    variables and objects to `None`—or objects like it, which are called
    singletons—using `==`; you should always use `is`.
"""
