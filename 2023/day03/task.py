"""
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source,
but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone!
The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the
engine, but nobody can figure out which one. If you can add up all the part
numbers in the engine schematic, it should be easy to work out which part
is missing.

The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols you
don't really understand, but apparently any number adjacent to a symbol,
even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)
"""
import dataclasses
import re
from typing import TypedDict


def task1(input_lines: list[str]):
    """
    Of course, the actual engine schematic is much larger. What is the sum of
    all of the part numbers in the engine schematic?
    """
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbs = re.compile(r"[^.]")
    
    sum = 0
    for lidx, line in enumerate(input_lines):
        # loop through the file
        part_num = ''
        cidx = 0
        # loop through the lines
        while cidx < len(line):
            char = line[cidx]
            
            # find/build possible part numbers
            if char in nums:
                pidx = cidx
                while True:
                    char = line[cidx]
                    if char not in nums:
                        break
                    part_num += char
                    cidx += 1
                    if cidx >= len(line):
                        break
            else:
                # print(lidx, cidx, char)
                cidx += 1
                continue
            
            # print("Found part!:", part_num, f"Length: {len(part_num)}",f"\tIndex: ({lidx+1},{pidx})")
            
            # check if part number is valid
            valid = False
            for l in range(max(lidx - 1, 0), min(lidx + 2, len(input_lines))):
                for p in range(max(pidx - 1, 0), min(pidx + len(part_num) + 1, len(line))):
                    # check only *around* the number
                    if l != lidx or p not in range(pidx, pidx + len(part_num)):
                        if symbs.match(input_lines[l][p]):
                            valid = True
                            break
                if valid:
                    break
            if valid:
                # print("\tValid part! ", part_num, f" \tIndex: ({lidx + 1},{pidx})")
                sum += int(part_num)
            else:
                # print("\tInvalid part", part_num, f" \tIndex: ({lidx + 1},{pidx})")
                pass
            part_num = ''
    
    print(sum)


"""
The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still
wrong? Fortunately, the gondola has a phone labeled "help", so you pick it
up and the engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving
with the other. You're going so slowly that you haven't even left the
station. You exit the gondola.
"""


class Index(TypedDict):
    row: int
    col: int


class Symbol(Index, total=False):
    symbol: str


class Part:
    def __init__(self, part_num: str, part_index: dict[str, int]):
        self.part_num: str = part_num
        self.part_index: Index = part_index
        self.line = part_index['row']
        self.start = part_index['col']
        self.end = self.start + len(self.part_num)
    
    def lookaround(self, input_lines: list[str], search_pattern: re.Pattern) -> list[Symbol]:
        symbs = []
        for l in range(max(self.line - 1, 0), min(self.line + 2, len(input_lines))):
            for p in range(max(self.start - 1, 0), min(self.end + 1, len(input_lines[l]))):
                # check only *around* the number
                if l != self.line or p not in range(self.start, self.end):
                    if m := search_pattern.match(input_lines[l][p]):
                        symbs.append(Symbol(row=l, col=p, symbol=m.group()))
        return symbs
    
    def get_part_num(self) -> int:
        return int(self.part_num)
    
    def __str__(self):
        return f"{self.part_num:<3} ({self.part_index['row'] + 1:0>3}, {self.part_index['col'] + 1:0>3})"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return (isinstance(other, Part) and
                self.get_part_num() == other.get_part_num() and
                self.part_index == other.part_index)


class Gear:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.connected_parts: list[Part] = []
    
    def add_part(self, part: Part):
        if part not in self.connected_parts:
            self.connected_parts.append(part)
    
    def gear_ratio(self):
        if len(self.connected_parts) != 2:
            return 0
        
        ratio = 1
        for part in self.connected_parts:
            ratio *= part.get_part_num()
        return ratio
    
    def __str__(self):
        return (f"@({self.row + 1:0>3}, {self.col + 1:0>3}) \t{self.gear_ratio()}\n"
                f"\t{len(self.connected_parts)} Parts: {self.connected_parts}")
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Gear) and self.row == other.row and self.col == other.col


def task2(input_lines: list[str]):
    """
    The missing part wasn't the only issue - one of the gears in the engine is
    wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.

    This time, you need to find the gear ratio of every gear and add them all
    up so that the engineer can figure out which gear needs to be replaced.
    """
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    gears: list[Gear] = []
    for lidx, line in enumerate(input_lines):
        # loop through the file
        part_num = ''
        cidx = 0
        # loop through the lines
        while cidx < len(line):
            char = line[cidx]
            
            # find/build possible part numbers
            if char in nums:
                pidx = cidx
                while True:
                    char = line[cidx]
                    if char not in nums:
                        break
                    part_num += char
                    cidx += 1
                    if cidx >= len(line):
                        break
            else:
                # print(lidx, cidx, char)
                cidx += 1
                continue
            
            # print("Found part!:", part_num, f"Length: {len(part_num)}",f"\tIndex: ({lidx+1},{pidx})")
            part = Part(part_num, {'row': lidx, 'col': pidx})
            
            # check if part is in a gear
            for symb in part.lookaround(input_lines, re.compile(r"[*]")):
                print("Might be in a gear-", part)
                gear = Gear(symb['row'], symb['col'])
                if gear in gears:
                    gears[gears.index(gear)].add_part(part)
                else:
                    gear.add_part(part)
                    gears.append(gear)
            else:
                # print("\tNot in a gear ", part_num, f" \tIndex: ({lidx + 1},{pidx})")
                pass
            part_num = ''
    sum = 0
    for gear in gears:
        print(gear)
        sum += gear.gear_ratio()
    
    print(sum)
