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
What to do instead?
    This one's easy: just listen to the style guides! You should never compare
    variables and objects to `None`—or objects like it, which are called
    singletons—using `==`; you should always use `is`.
"""
