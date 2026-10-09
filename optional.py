############################
# Optional Challenges
def nth_generalized_number(n, zeroth, first):
    """
    Context:
    The Fibonacci sequence is a member in a family of sequences defined by a recurrence.

    Another sequence is the Lucas Sequence, where its numbers are defined by the following:

        L_i = L_{i - 1} + L_{i - 2}

    nth_lucas_number(0) = 2
    nth_lucas_number(1) = 1
    nth_lucas_number(2) = 3
    nth_lucas_number(5) = 11
    nth_lucas_number(8) = 47

    Task:
        Abstract over your nth_fibonacci_number function to define this `nth_generalized_number`. Modify the accepted arguments to change the initial numbers
    """

    raise NotImplementedError()


def fast_nth_generalized_number(n, zeroth, first, cache={}):
    """
    Context:
        Looking closely at the `nth_generalized_number`, we see that we might end up
        repeating a lot of work. Draw out a call tree of `nth_generalized_number`(5) to convince yourself of this.

        One way to optimize this is to use a "cache" so that we can reuse already-computed values.

    Task:
        Modify your `nth_generalized_number` to accept a cache value

    Hint: think about what you've learned in SWC and how you can efficiently "look up" values

    """
    raise NotImplementedError()


def two_sum(in_arr, target_value):
    """
    Task:
        given an array of integers and a target value, return the indices corresponding to the integers that sum
        to the target value.

        If there is more than one solution you may return any valid set of indices. If there are no pairs satisfying this,
        return a None
    """
    raise NotImplementedError()


def test_fibonacci_generalized():
    # Test unoptimized
    assert nth_generalized_number(8, 0, 1) == 21
    assert nth_generalized_number(10, 0, 1) == 55

    # Test Optimized
    assert fast_nth_generalized_number(8, 0, 1) == 21
    assert fast_nth_generalized_number(10, 0, 1) == 55


def test_lucas_generalized():
    # Test unoptimized
    assert nth_generalized_number(8, 2, 1) == 47
    assert nth_generalized_number(10, 2, 1) == 123

    # Test Optimized
    assert fast_nth_generalized_number(8, 2, 1) == 47
    assert fast_nth_generalized_number(10, 2, 1) == 123


def test_mixed():
    """
    Task:
        can you identify WHY the second call fails even though we've established that our code from before was correct?
        How do you change the function to make it correct?

    Hint:
        try smaller `n` and print the cache. In the future we will introduce debuggers, which will make your lives
        easier
    """
    assert fast_nth_generalized_number(10, 0, 1) == 55
    assert fast_nth_generalized_number(10, 2, 1) == 123


def test_two_sum():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    assert sorted(two_sum([-1, 5, 1], 0)) == [0, 2]
    assert sorted(two_sum([-1, 5, 1], 100)) is None  # Do you know why we do an `is None` instead of `== None` ?


if __name__ == "__main__":
    test_fibonacci_generalized()
    test_lucas_generalized()
    test_mixed()
    test_two_sum()
