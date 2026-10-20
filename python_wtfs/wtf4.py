"""
Python WTFs: Fun with `is`
"""

"""
NOTE:
    These exercises might not work depending on what Python implementation
    you're using! These exercises were written based on CPython. CPython is the
    default Python implementation. If you don't know what Python implementation
    you're using, it's almost certainly CPython.
"""

"""
NOTE:
    Before we get to these problems, we need to go over a new Python function we
    haven't seen yet.

    That function is `exec`. The `exec` function is simple. It executes Python
    code. If you supply it a string of Python code, it'll execute it. Here,
    we're using it to simulate the Python REPL. Running `exec("a = 1")` is
    effectively the same as running `>>> a = 1` in the Python REPL.
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

"""
WTF??? Why did that happen?
    Ok so a lot happened in this file. Let's go over all of it.

    To recap our initial explanations:
        -   `==` is the equivalency operator and checks if the two objects are
            equivalent, according to some definition of equivalence.
        -   `is` is the identity operator. It checks to see if the two objects
            are the same object.

    So, what's going on with the integers? It's easiest if we start with
    `exec("lhs = 257")` and `exec("rhs = 257")`. What's happening with these
    two statements is that Python is creating two new integer objects, `lhs` and
    `rhs`, and setting the value of both to `257`. The key concept is that we're
    creating two new objects that both just so happen to have the same value.
    They are NOT the same object. The same thing happens when we do
    `exec("lhs = -6")` and `exec("rhs = -6")`.

    Ok, so then what's going on with `exec("lhs = 2")`, `exec("rhs = 2")`,
    `exec("lhs = 256")`, `exec("rhs = 256")`, `exec("lhs = -5")`, and
    `exec("rhs = -5")`? The answer is that CPython automatically creates objects
    for every integer between -5 and 256. Then, instead of creating a new object
    whenever one of those variables is used, CPython points to those
    automatically-created objects; CPython does NOT create new objects for those
    integers. This ONLY happens for integers between -5 and 256.

    If that's the case, what's going on in the cases without the `exec`
    function? This goes back to some weirdness with how Python works. Typically,
    you'll hear the Python is an interpreted language; that Python runs by
    stepping one line at a time and executing each line. And this is mostly
    true. Python is interpreted. But, Python is not only interpreted; it is also
    compiled. Specifically, when you run a Python file, the Python interpreter
    first compiles the file to bytecode and then interprets the bytecode. It
    does this to optimize the code. For us, what this means is that when we run
    the statements that don't use `exec`, the Python interpreter compiles the
    file and in doing so, optimizes the code to just create a single `257` and a
    single `-6` object that `lhs` and `rhs` both point to. It does this because
    it takes up more memory to create separate objects for both of the `257`s
    and both `-6`s.
"""

"""
What to do instead?
    NEVER use `is` to compare integers. Just don't do it.
"""
