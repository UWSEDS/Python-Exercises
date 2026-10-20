"""
Python WTFs: Fun with `is`
"""

"""
Before we get to these problems, we need to go over a couple of Python functions
and what they do.

The first function is `exec`. The `exec` function is simple. It executes Python
code. If you supply it a string of Python code, it'll execute it. We're using it
here to simulate the Python REPL. Running `exec("a = 1")` is effectively the
same as running `>>> a = 1` in the Python REPL.

The second function is `id`. Every object in Python has an ID, and the function
`id` returns that ID to us.
"""

"""
Problem 1:
    Uncomment the four statements below. What happens when you run the file?
"""

# lhs = [1, 2, 3]
# rhs = lhs
# print(lhs == rhs)
# print(lhs is rhs)

"""
Explanation 1:
    The two statements both print `True`! The reason why is because the two
    lists contain the same data AND also are the same exact object. Assigning a
    variable (`rhs`) to a different variable (`lhs`) doesn't create a new object
    with the same data; it makes the two variables contain the same object (so
    `rhs` and `lhs` contain the same object).
"""

"""
Problem 2:
    Recomment the four statements above and uncomment the four below. Now what
    happens when you run the file?
"""

# lhs = [1, 2, 3]
# rhs = [1, 2, 3]
# print(lhs == rhs)
# print(lhs is rhs)

"""
Explanation 2:
    The two statements both print `True`! The reason why is because the two
    lists contain the same data AND also are the same exact object. Assigning a
    variable (`rhs`) to a different variable (`lhs`) doesn't create a new object
    with the same data; it makes the two variables contain the same object (so
    `rhs` and `lhs` contain the same object).
"""

lhs = 2
rhs = 2

print(lhs == rhs)
print(lhs is rhs)

lhs = 256
rhs = 256

print(lhs == rhs)
print(lhs is rhs)

lhs = 257
rhs = 257

print(lhs == rhs)
print(lhs is rhs)

lhs = -5
rhs = -5

print(lhs == rhs)
print(lhs is rhs)

lhs = -6
rhs = -6

print(lhs == rhs)
print(lhs is rhs)

print(257 is 257)
