more = [x + 1 for x in [1, 2, 3, 4]]        # List, in order, the values that x takes at each step. 1, 2, 3, then 4.
print()                                     # What is the value of more at this point? more: [2, 3, 4, 5]


def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and [1,1], [2,4], [3,9], [4, 16]
                                           # the corresponding return value.


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? squares = [1, 4, 9, 16]

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. [0, False], [1, False], [2, False], [3, True], [4, True]


answer = [x for x in range(5) if check(x)]   # What is the value of answer? answer = [3,4], range doesn't check 5 (upper limit)
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.  [3,4], [4,5]


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 1 > 2 = False, 2 > 2 = False, 3 > 2 = True


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? The answer = [4,5]
print()