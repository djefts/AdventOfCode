"""

"""


def task1(input_lines: list[str]):
    """
    
    """
    times = input_lines[0].split(":")[1].split()
    records = input_lines[1].split(":")[1].split()
    assert len(times) == len(records)
    races = len(times)
    
    prod = 1
    for race in range(races):
        time = int(times[race])
        record = int(records[race])
        ways_to_win = 0
        for i in range(1, time - 1):
            held = i
            speed = held
            distance = speed * (time - held)
            if distance > record:
                ways_to_win += 1
        prod *= ways_to_win
    print(prod)


"""

"""


def task2(input_lines: list[str]):
    """
    
    """
    time = int(''.join(input_lines[0].split(":")[1].split()))
    record = int(''.join(input_lines[1].split(":")[1].split()))
    
    win_low = 0
    for i in range(1, time - 1):
        held = i
        speed = held
        distance = speed * (time - held)
        if distance > record:
            win_low = i
            break
    win_high = 0
    for i in range(time, 1, -1):
        held = i
        speed = held
        distance = speed * (time - held)
        if distance > record:
            win_high = i
            break
    print(win_high - win_low + 1)
