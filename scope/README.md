# Python scope exercises

This section of the exercises focuses on scope rules in Python!
In programming, scope refers to two related concepts in programming.
The first definition is that scope refers to the portion of a program where a given variable, function, etc. is defined or valid.
The second definition of scope if the set of variables, functions, classes, etc. that are defined and valid at any given location in a program.
We're going to be focusing more on the second definition, but we'll bring everything back around to the first definition too!

For a bit of practical example, consider the following block of code:

```python
x = 1
y = 2

def function():
    z = 3
```

In this code, we have two different scopes visible: an outer and an inner scope.
The inner scope in this case is just line 5 while the outer scope is the first 4 lines.
One way to think about this is boxes:

```raw
┌──────────────────────────────┐
│outer_scope                   │
│                              │
│               x = 1          │
│                              │
│  ┌────────────┐              │
│  │inner_scope │       y = 2  │
│  │            │              │
│  │  z = 3     │ function     │
│  │            │              │
│  └────────────┘              │
└──────────────────────────────┘
```

The variable `z` is only defined within the inner scope, while `x`, `y`, and the function `function` are all defined within the outer scope.

```raw
┌───────────────────────────────────────┐
│outer_scope                            │
│                                       │
│                                       │
│                                       │
│  ┌──────────────┐   ┌──────────────┐  │
│  │inner_scope_1 │   │inner_scope_2 │  │
│  │              │   │              │  │
│  │              │   │              │  │
│  │              │   │              │  │
│  └──────────────┘   └──────────────┘  │
└───────────────────────────────────────┘
```

```raw
┌────────────────────────────────────────────┐
│outer_scope                                 │
│                                            │
│                          ┌──────────────┐  │
│                          │inner_scope_3 │  │
│  ┌───────────────────┐   │              │  │
│  │inner_scope_1      │   │              │  │
│  │                   │   │              │  │
│  │                   │   │              │  │
│  │                   │   │              │  │
│  │                   │   │              │  │
│  │                   │   │              │  │
│  │  ┌──────────────┐ │   └──────────────┘  │
│  │  │inner_scope_2 │ │                     │
│  │  │              │ │   ┌──────────────┐  │
│  │  │              │ │   │inner_scope_4 │  │
│  │  │              │ │   │              │  │
│  │  │              │ │   │              │  │
│  │  └──────────────┘ │   │              │  │
│  └───────────────────┘   └──────────────┘  │
└────────────────────────────────────────────┘
```
