# Python-Exercises

Exercises following the [Python SWC course](https://swcarpentry.github.io/python-novice-inflammation/)

## Layout

A quick introduction to the files in this repository:

- `exercises.py`: contains exercises you should be able to solve after the SWC. There are non-exhaustive tests in the second half of the file that you can test your implementation against

- `optional.py`: contains optional exercises for those who are already more familiar with Python and want a challenge.

- `refactoring.py`: code from [alan-turing-institute/bad-boids/](https://github.com/alan-turing-institute/bad-boids/blob/main/boids.py) that we've annotated with things to think about as you improve the code. The authors have a [GitHub branch](https://github.com/alan-turing-institute/bad-boids/tree/better_boids/boids) with their recommended refactoring, but some of those concepts are well beyond the scope of what we want to cover now. That said, feel free to take a look through!

- `python_wtfs`: a folder of wacky exercises that show unexpected ways Python can misbehave.

## `exercises.py`

To run the code you have a few options:

- run `python` from the terminal, import one of the test functions, and run it.

```
from exercises import test_every_other_element
test_every_other_element()
```

- run the entire file like `python exercises.py`, but this runs all the tests that are uncommented at the very bottom of the file, even the ones you haven't completed yet.

---

If your implementation is correct, you won't see anything on your screen, but if your code was incorrect you might see something like:

```
Traceback (most recent call last):
File "<python-input-1>", line 1, in <module>
test_every_other_element()
~~~~~~~~~~~~~~~~~~~~~~~~^^

File "/home/iq/personal/Python-Exercises/exercises.py", line 124, in test_every_other_element
assert every_other_element([1, 2, 3]) == [2]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

## Learning And productivity

Some of these exercises are _hard_ and you shouldn't feel bad about taking a lot of time working on them. Struggling (productively) is a part of the learning process. If you find yourself spinning your wheels you should take a quick walk and return to the problem(s) later. The goal isn't to be _done_ with the exercises. It's to _understand_ why your solution works and how the core ideas can be transferred to other problems.
