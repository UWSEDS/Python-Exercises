"""
Python WTFs: Comparing to `None`
"""

"""
Problem 1:
    Python style guides will often tell you:
        "Don't compare to None with x == None. Use x is None."
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
    Do the statements evaluate equivalently?
"""

# from wtf3_lib import Foo
# foo = Foo()
# print(foo == None)
# print(foo is None)
