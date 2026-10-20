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
    The two statements print different things! The first prints `True` while the
    second prints `False`. The reason why is because the two lists contain the
    same data BUT ARE NOT the same exact object. Here, we created two separate
    list objects that just so happen to have the same data.

    This shows us the difference between `==` and `is`. `==` is the equality
    operator and usually checks to see that the two objects contain equivalent
    values, whatever that might mean—however, we showed in the previous file
    that equality can be redefined to mean whatever we want. `is`, on the other
    hand, checks whether or not the two underlying objects are the same. In this
    case, they're not.
"""

"""
Problem 3:
    The instructions on this file are all gonna be really similar. Recomment the
    four statements above and uncomment the four below. Now what happens when
    you run the file?
"""

# lhs = 2
# rhs = 2
# print(lhs == rhs)
# print(lhs is rhs)

"""
Explanation 3:
    For now, just note that these two printed the same value and try to think of
    what the general principle behind this might be. Maybe integers that have
    the same value are all the same exact object?
"""

"""
Problem 4:
    It's time to start using the function we mentioned at the top of the file.
    Here, we're using `exec` to simulate running these lines in the Python REPL.
    Recomment the four statements above and uncomment the four below. Now what
    happens when you run the file?
"""

# exec("lhs = 2")
# exec("rhs = 2")
# print(lhs == rhs)
# print(lhs is rhs)

"""
Problem 5:
    Let's try with a different number. Recomment the four statements above and
    uncomment the four below. Now what happens when you run the file?
"""

# exec("lhs = 256")
# exec("rhs = 256")
# print(lhs == rhs)
# print(lhs is rhs)

"""
Problem 6:
    Alright, let's try another one. Recomment the four statements above and
    uncomment the four below. Now what happens when you run the file?
"""

# exec("lhs = 257")
# exec("rhs = 257")
# print(lhs == rhs)
# print(lhs is rhs)


"""
Explanation 6:
    Pause. Something different happened this time, didn't it?

    Before we explain what's happening, let's try a couple more of these.
"""

"""
Problem 7:
    Recomment the four statements above and uncomment the four below. Now what
    happens when you run the file?
"""

# exec("lhs = -5")
# exec("rhs = -5")
# print(lhs == rhs)
# print(lhs is rhs)

"""
Problem 8:
    Recomment the four statements above and uncomment the four below. Now what
    happens when you run the file?
"""

# exec("lhs = -6")
# exec("rhs = -6")
# print(lhs == rhs)
# print(lhs is rhs)

"""
Problem 9:
    Let's stop using `exec` and go back to just executing these statements in
    the file instead of simulating running them in a repl. Recomment the four
    statements above and uncomment the eight below. Now what happens when you
    run the file?
"""

# lhs = 257
# rhs = 257
# print(lhs == rhs)
# print(lhs is rhs)
# lhs = -6
# rhs = -6
# print(lhs == rhs)
# print(lhs is rhs)
