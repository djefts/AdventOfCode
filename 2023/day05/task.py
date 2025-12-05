"""

"""
import operator
import re
from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Seed:
    def __init__(self, seed_num: int):
        self.seed_num = seed_num
        self.soil = seed_num
        self.fertilizer = seed_num
        self.water = seed_num
        self.light = seed_num
        self.temperature = seed_num
        self.humidity = seed_num
        self.location = seed_num
    
    def __eq__(self, other):
        return self.seed_num == other.seed_num
    
    def __repr__(self):
        output = f"Seed #{self.seed_num}->"
        output += ', '.join([f"{self.soil=}", f"{self.fertilizer=}", f"{self.water=}", f"{self.light=}",
                             f"{self.temperature=}", f"{self.humidity=}", f"{self.location=}"])
        return output


def parse_map(input_lines, start_line):
    output = []
    while start_line < len(input_lines) and input_lines[start_line] != "":
        regex = re.match(r"(\d+) (\d+) (\d+)", input_lines[start_line]).groups()
        # print(regex)
        
        destination = int(regex[0])
        source = int(regex[1])
        size = int(regex[2])
        
        start_line += 1
        output.append([destination, source, size])
    return output, start_line


def task1(input_lines: list[str]):
    """
    The almanac (your puzzle input) lists all of the seeds that need to be
    planted. It also lists what type of soil to use with each kind of seed,
    what type of fertilizer to use with each kind of soil, what type of water
    to use with each kind of fertilizer, and so on. Every type of seed, soil,
    fertilizer and so on is identified with a number, but numbers are reused by
    each category - that is, soil 123 and fertilizer 123 aren't necessarily
    related to each other.
    
    The rest of the almanac contains a list of maps which describe how to convert
    numbers from a source category into numbers in a destination category. That is,
    the section that starts with seed-to-soil map: describes how to convert a seed
    number (the source) to a soil number (the destination). This lets the gardener
    and his team know which soil to use with which seeds, which water to use with
    which fertilizer, and so on.

    Rather than list every source number and its corresponding destination number
    one by one, the maps describe entire ranges of numbers that can be converted.
    Each line within a map contains three numbers: the destination range start,
    the source range start, and the range length.
    
    The gardener and his team want to get started as soon as possible, so they'd
    like to know the closest location that needs a seed. Using these maps, find
    the lowest location number that corresponds to any of the initial seeds. To
    do this, you'll need to convert each seed number through other cats until
    you can find its corresponding location number. In this example, the corresponding types are:
        Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
        Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
        Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
        Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    So, the lowest location number in this example is 35.
    """
    target_seed_nums = [int(s) for s in input_lines[0].split(": ")[1].split(" ")]
    
    seeds = []
    for i in target_seed_nums:
        seeds.append([i] * 8)
    print(target_seed_nums)
    
    lidx = 1
    cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    for cidx in range(1, len(cats)):
        dest_cat = cidx  # soil
        sour_cat = cidx - 1  # seed_num
        print(f"Mapping {cats[dest_cat]} to {cats[sour_cat]}")
        maps, lidx = parse_map(input_lines, lidx + 2)
        for map in maps:
            d = int(map[0])  # map from
            s = int(map[1])  # map onto
            r = int(map[2])  # range length
            for seed in seeds:
                if seed[sour_cat] in range(s, s + r):
                    print(
                            f"\tMapping Seed #{seed[0]}'s {cats[dest_cat]} from {seed[dest_cat]} to {seed[sour_cat] - s + d}")
                    seed[dest_cat] = seed[sour_cat] - s + d
                    for c in range(cidx + 1, len(cats)):
                        seed[c] = seed[sour_cat] - s + d
    
    for seed in seeds:
        print(seed)
    print(min(seed[7] for seed in seeds))


"""

"""


# noinspection DuplicatedCode
def task2(input_lines: list[str]):
    """

    """
    target_seed_nums = [int(s) for s in input_lines[0].split(": ")[1].split(" ")]
    
    seed_ranges = []
    for i in range(0, len(target_seed_nums), 2):
        seed_ranges.append([[target_seed_nums[i], target_seed_nums[i] + target_seed_nums[i + 1] - 1]] * 8)
    print(seed_ranges)
    
    lidx = 1
    cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    for cidx in range(1, len(cats)):
        dest_cat = cidx  # soil
        sour_cat = cidx - 1  # seed_num
        print(f"Mapping {cats[dest_cat]} to {cats[sour_cat]}")
        maps, lidx = parse_map(input_lines, lidx + 2)
        for map in maps:
            d = int(map[0])  # map from
            s = int(map[1])  # map onto
            r = int(map[2])  # range length
            for seed in seed_ranges:
                if seed[sour_cat][0] in range(s, s + r):
                    # seed_range source start is in the map range
                    print(f"\tMapping Seed #{seed[0][0]}'s {cats[dest_cat]} from {seed[dest_cat]} "
                          f"to {[seed[sour_cat][0] - s + d, seed[sour_cat][1]]}")
                    seed[dest_cat][0] = seed[sour_cat][0] - s + d
                    for c in range(cidx + 1, len(cats)):
                        print(f"\t  Copying Seed #{seed[0][0]}'s {cats[c]} to {[seed[sour_cat][0], seed[sour_cat][1]]}")
                        seed[c][0] = seed[sour_cat][0]
                if seed[sour_cat][1] in range(s, s+r):
                    if seed[sour_cat][0] in range(s, s + r):
                        # seed_range source start is in the map range
                        print(f"\tMapping Seed #{seed[0][0]}'s {cats[dest_cat]} from {seed[dest_cat]} "
                              f"to {[seed[sour_cat][0], seed[sour_cat][1] - s + d]}")
                        seed[dest_cat][1] = seed[sour_cat][1] - s + d
                        for c in range(cidx + 1, len(cats)):
                            print(
                                f"\t  Copying Seed #{seed[0][0]}'s {cats[c]} to {[seed[sour_cat][0], seed[sour_cat][1]]}")
                            seed[c][1] = seed[sour_cat][1]
                print(f"\tPost:", seed)
    
    for seed in seed_ranges:
        print(seed)
    print(min(seed[7] for seed in seed_ranges))


def task2_brute(input_lines: list[str]):
    """
    
    """
    target_seed_nums = [int(s) for s in input_lines[0].split(": ")[1].split(" ")]
    
    seeds = []
    for i in range(0, len(target_seed_nums), 2):
        for j in range(target_seed_nums[i], target_seed_nums[i] + target_seed_nums[i + 1]):
            seeds.append([j] * 8)
        print(f"Created {len(seeds)} seeds")
    print([s[0] for s in seeds])
    
    lidx = 1
    cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    for cidx in range(1, len(cats)):
        dest_cat = cidx  # soil
        sour_cat = cidx - 1  # seed_num
        print(f"Mapping {cats[dest_cat]} to {cats[sour_cat]}")
        maps, lidx = parse_map(input_lines, lidx + 2)
        for map in maps:
            d = int(map[0])  # map from
            s = int(map[1])  # map onto
            r = int(map[2])  # range length
            for seed in seeds:
                if seed[sour_cat] in range(s, s + r):
                    print(
                            f"\tMapping Seed #{seed[0]}'s {cats[dest_cat]} from {seed[dest_cat]} to {seed[sour_cat] - s + d}")
                    seed[dest_cat] = seed[sour_cat] - s + d
                    for c in range(cidx + 1, len(cats)):
                        seed[c] = seed[sour_cat] - s + d
    
    for seed in seeds:
        print(seed)
    print(min(seed[7] for seed in seeds))
