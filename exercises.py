def every_other_element(arr):
    """
    Task:
        Given an array return the 2i+1th element where i takes values of {0, 1, ...}

    Hint: This can be done in a one-liner using a list comprehension but you're welcome to use a for-loop, too
    """
    raise NotImplementedError()


def is_palindrome(in_str):
    """
    Task:

    Determine if an input string is a palindrome. There are multiple ways of doing this but you should try doing this with
    a for-loop (you will have to do some indexing) and using string slicing.

    Additional task:
        - does your solution work with strings and lists?
    """
    raise NotImplementedError()


def fizzbuzz(n):
    """
    Task:
    Given an integer n, return a string array answer (1-indexed) where:

         answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
         answer[i] == "Fizz" if i is divisible by 3.
         answer[i] == "Buzz" if i is divisible by 5.
         answer[i] == i (as a string) if none of the above conditions are true.

    """
    raise NotImplementedError()


def happy_numbers(n):
    """

    Context:

    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.

        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

        Those numbers for which this process ends in 1 are happy.

    Task:
        Return true if n is a happy number, and false if not.
    """
    raise NotImplementedError()


def nth_fibonacci_number(n):
    """
    Context:
    A Fibonacci number is a number where the i-th Fibonacci number is the sum of the i-1th and i-2 Fibonacci numbers i.e.

        F_i = F_{i - 1} + F_{i - 2}

    A natural way of calculating this is via recursion.

    Task:
        When the input is 0 or negative, it should return 0. When the input is 1 or 2 it should return 1. In all other cases it should follow the recurrence formula we specified earlier.

        You may assume that the input number is greater-than-or-equal-to 0
    """
    raise NotImplementedError()

def safe_divide(numerator, denominator):
    """
    Context:

        there are multiple ways to handle errors:
            - look-before-you-leap)
            - 
    
        Division by zero in python throws an exception: ZeroDivisionError. However, we might want to recover from this!

        https://realpython.com/python-lbyl-vs-eafp/

    Task:
        
            
        Do not check if the denominator is zero. Instead, we want to 
    """

"""
Simple test cases that you should add to! 
"""

#####################################
# Simple test Cases:
# Note: the following tests do not test all the edge-cases! You should think through
#       them and add any others that might be necessary
#####################################

def test_every_other_element():
    assert every_other_element([1, 2, 3]) == [2]
    assert every_other_element(["uh-oh"]) == []

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("wow") == True
def test_fizzbuzz():
    assert fizzbuzz(3) == ["1","2","Fizz"]
    assert fizzbuzz(5) == ["1","2","Fizz","4","Buzz"]

def test_happy_numbers():
    assert happy_numbers(4) == False
    assert happy_numbers(13) == True

def test_fibonacci():
    assert nth_fibonacci_number(8) == 21
    assert nth_fibonacci_number(10) == 55

if __name__ == "__main__":
    test_every_other_element()
    test_is_palindrome()
    test_fizzbuzz()
    test_happy_numbers()
    test_fibonacci()


