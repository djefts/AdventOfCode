"""
You ride the camel through the sandstorm and stop where the ghost's maps told you to
stop. The sandstorm subsequently subsides, somehow seeing you standing at an oasis!

The camel goes to get some water and you stretch your neck. As you look up, you
discover what must be yet another giant floating island, this one made of metal! That
must be where the parts to fix the sand machines come from.

There's even a hang glider partially buried in the sand here; once the sun rises and
heats up the sand, you might be able to use the glider and the hot air to get all the
way up to the metal island!

While you wait for the sun to rise, you admire the oasis hidden here in the middle of
Desert Island. It must have a delicate ecosystem; you might as well take some
ecological readings while you wait. Maybe you can report any environmental
instabilities you find to someone so the oasis can be around for the next
sandstorm-worn traveler.

You pull out your handy Oasis And Sand Instability Sensor and analyze your
surroundings. The OASIS produces a report of many values and how they are changing over
time (your puzzle input). Each line in the report contains the history of a single
value.
"""


def calc_diffs(data: list[int]) -> list[int]:
    diffs = []
    for i in range(len(data) - 1):
        diffs.append(data[i + 1] - data[i])
    print(diffs)
    
    if not done(diffs):
        diffs = calc_diffs(diffs)
    return data + [data[-1] + diffs[-1]]


def done(data: list[int]) -> bool:
    data = iter(data)
    try:
        first = next(data)
    except StopIteration:
        return True
    return all(first == x for x in data)


def task1(input_lines: list[str]):
    """
    To best protect the oasis, your environmental report should include a prediction of
    the next value in each history. To do this, start by making a new sequence from the
    difference at each step of your history. If that sequence is not all zeroes, repeat
    this process, using the sequence you just generated as the input sequence. Once all
    of the values in your latest sequence are zeroes, you can extrapolate what the next
    value of the original history should be.

    In the above dataset, the first history is 0 3 6 9 12 15. Because the values
    increase by 3 each step, the first sequence of differences that you generate will
    be 3 3 3 3 3. Note that this sequence has one fewer value than the input sequence
    because at each step it considers two numbers from the input. Since these values
    aren't all zero, repeat the process: the values differ by 0 at each step, so the
    next sequence is 0 0 0 0. This means you have enough information to extrapolate
    the history!
    """
    sum = 0
    for line in input_lines:
        l = [int(x) for x in line.split()]
        print(l)
        o = calc_diffs(l)
        print(f"output: {o}\n")
        sum += o[-1]
    print(f"{sum=}")


"""
Of course, it would be nice to have even more history included in your report. Surely
it's safe to just extrapolate backwards as well, right?
"""


def task2(input_lines: list[str]):
    """
    For each history, repeat the process of finding differences until the sequence of
    differences is entirely zero. Then, rather than adding a zero to the end and
    filling in the next values of each previous sequence, you should instead add a zero
    to the beginning of your sequence of zeroes, then fill in new first values for each
    previous sequence.
    
    Adding the new values on the left side of each sequence from bottom to top
    eventually reveals the new left-most history value: 5.

    Doing this for the remaining example data above results in previous values of -3
    for the first history and 0 for the second history. Adding all three new values
    together produces 2.
    """
    sum = 0
    for line in input_lines:
        l = [int(x) for x in line.split()]
        l.reverse()
        print(l)
        o = calc_diffs(l)
        print(f"output: {o}\n")
        sum += o[-1]
    print(f"{sum=}")
