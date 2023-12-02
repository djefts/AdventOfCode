import re


def task1(input_lines: list[str]):
    """
    The newly-improved calibration document consists of lines of text; each
    line originally contained a specific calibration value that the Elves now
    need to recover. On each line, the calibration value can be found by
    combining the first digit and the last digit (in that order) to form a
    single two-digit number.
    """
    sum = 0
    for line in input_lines:
        nums = re.findall(r'\d', line)
        # print(nums)
        sum += int(nums[0] + nums[-1])
    
    print(sum)


def task2(input_lines):
    """
    Your calculation isn't quite right. It looks like some of the digits are
    actually spelled out with letters: one, two, three, four, five, six, seven,
    eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first and
    last digit on each line.
    """
    digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sum = 0
    for line in input_lines:
        pattern = r'\d|' + f"{'|'.join(digit_words)}"
        
        num1 = re.search(pattern, line).group(0)
        if num1 in digit_words:
            num1 = str(digit_words.index(num1))
        
        num2 = re.search(f".*({pattern})(?!{pattern}).*$", line).group(1)
        if num2 in digit_words:
            num2 = str(digit_words.index(num2))
        # print(f"{line=} :: {num1=} {num2=}")
        sum += int(num1 + num2)
        
    print(sum)
