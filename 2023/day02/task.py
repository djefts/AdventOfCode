"""
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island
floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf
runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the
situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to
play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this
game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about
the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random
cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
"""
import re


def task1(input_lines: list[str]):
    """
    The Elf would first like to know which games would have been possible if
    the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    """
    sum = 0
    for line in input_lines:
        game_id = int(line.split(':')[0].split(" ")[1])
        valid = True
        game = line.split(':')[1]
        sets = game.split(';')
        for set in sets:
            cubes = {"red": 0, "green": 0, "blue": 0}
            pulls = set.split(', ')
            for pull in pulls:
                pull = pull.strip().split(" ")
                cubes[pull[1]] = int(pull[0])
            if cubes['red'] > 12 or cubes['green'] > 13 or cubes['blue'] > 14:
                valid = False
        if valid:
            sum += game_id
        print("Game", game_id, valid, cubes)
    print(sum)


"""
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped;
however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!
"""


def task2(input_lines: list[str]):
    """
    As you continue your walk, the Elf poses a second question: in each game
    you played, what is the fewest number of cubes of each color that could
    have been in the bag to make the game possible?
    """
    sum = 0
    for line in input_lines:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_id = int(line.split(':')[0].split(" ")[1])
        game = line.split(':')[1]
        sets = game.split(';')
        cubes = {"red": 0, "green": 0, "blue": 0}
        for set in sets:
            # 3 blue, 4 red
            pulls = set.split(', ')
            for pull in pulls:
                # 3 blue
                pull = pull.strip().split(" ")
                value = int(pull[0])
                color = pull[1]
                cubes[color] = max(cubes[color], value)
        power = cubes['red'] * cubes['green'] * cubes['blue']
        print("Game", game_id, cubes, power)
        sum += power
    print(sum)
