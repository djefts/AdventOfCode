"""
You use the hang glider to ride the hot air from Desert Island all the way up to the
floating metal island. This island is surprisingly cold and there definitely aren't any
thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you
do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent
direction; maybe you can find someone at the hot springs and ask them where the
desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop
to admire some metal grass, you notice something metallic scurry away in your
peripheral vision and jump into a big pipe! It didn't look like any animal you've ever
seen; if you want a better look, you'll need to get ahead of it.
"""
from collections import Counter
import numpy as np
import matplotlib.path as mplPath

def find_start(maze: list[str]):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return [i, j]


def task1(input_lines: list[str]):
    """
    Scanning the area, you discover that the entire field you're standing on is densely
    packed with pipes; it was hard to tell at first because they're the same metallic
    silver color as the "ground". You make a quick sketch of all of the surface pipes
    you can see (your puzzle input).
    
    If you want to get out ahead of the animal, you should find the tile in the loop
    that is farthest from the starting position. Because the animal is in the pipe, it
    doesn't make sense to measure this by direct distance. Instead, you need to find
    the tile that would take the longest number of steps along the loop to reach from
    the starting point - regardless of which way around the loop the animal went.
    
    Find the single giant loop starting at S. How many steps along the loop does it
    take to get from the starting position to the point farthest from the starting
    position?
    """
    cur_pos = find_start(input_lines)
    print(f"Start: {cur_pos}")
    
    # path: {angle: (axis, change, dest)}
    directions = {
            "|": {3: (0, 1, 3), 1: (0, -1, 1)},
            "-": {2: (1, 1, 2), 4: (1, -1, 4)},
            "L": {3: (1, 1, 2), 4: (0, -1, 1)},
            "J": {3: (1, -1, 4), 2: (0, -1, 1)},
            "7": {1: (1, -1, 4), 2: (0, 1, 3)},
            "F": {1: (1, 1, 2), 4: (0, 1, 3)},
    }
    
    angle = 0
    if input_lines[cur_pos[0] - 1][cur_pos[1]] in ["|", "7", "F"]:
        # check North
        print("starting north")
        cur_pos[0] -= 1
        angle = 1
    elif input_lines[cur_pos[0] + 1][cur_pos[1]] in ["|", "J", "L"]:
        # check South
        print("starting south")
        cur_pos[0] += 1
        angle = 3
    elif input_lines[cur_pos[0]][cur_pos[1] + 1] in ["-", "J", "7"]:
        # check East
        print("starting east")
        cur_pos[1] += 1
        angle = 2
    elif input_lines[cur_pos[0]][cur_pos[1] - 1] in ["-", "L", "F"]:
        # check West
        print("starting west")
        cur_pos[1] -= 1
        angle = 4
    
    steps = 1
    cur_pipe = input_lines[cur_pos[0]][cur_pos[1]]
    while cur_pipe != "S":
        # print(f"{cur_pipe} @ {cur_pos} from {angle}")
        if cur_pipe == ".":
            print("LKHJASGD LIAQSKIJDGHUASLIDHlhkjgASDKLJHGASD")
            return
        
        # use directions dict to move
        source = directions[cur_pipe][angle]
        cur_pos[source[0]] += source[1]
        angle = source[2]
        
        # take a step
        cur_pipe = input_lines[cur_pos[0]][cur_pos[1]]
        steps += 1
    
    print(steps // 2)


"""
You quickly reach the farthest point of the loop, but the animal never emerges. Maybe
its nest is within the area enclosed by the loop?
"""


class Point:
    y: int
    x: int
    angle: 1 | 2 | 3 | 4
    
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        
    def __iter__(self):
        return iter([self.y, self.x])
    
    def __array__(self):
        return np.array([self.y, self.x])
    
    def __repr__(self):
        return f"[{self.y}, {self.x}]"
    
    def __eq__(self, other):
        return self.y == other.y and self.x == other.x
    
    def __getitem__(self, item):
        if item == 'y':
            return self.y
        elif item == 'x':
            return self.x
        elif item == 'angle':
            return self.angle
        else:
            raise TypeError
    
    def __setitem__(self, key, value):
        if key == 'y':
            self.y = value
        elif key == 'x':
            self.x = value
        elif key == 'angle':
            self.angle = value
        else:
            raise TypeError
    
    def copy(self):
        return Point(self.y, self.x)


def task2(input_lines: list[str]):
    """
    To determine whether it's even worth taking the time to search for such a nest, you
    should calculate how many tiles are contained within the loop.
    
    Figure out whether you have time to search for the nest by calculating the area
    within the loop. How many tiles are enclosed by the loop?
    """
    tiles = len(input_lines) * len(input_lines[0])
    print(f"{tiles} total tiles.")
    pipe_tiles = []
    
    cur_pos: Point = Point(*find_start(input_lines))
    print(f"Start: {cur_pos}")
    pipe_tiles.append(cur_pos)
    
    # path: {angle: (axis, change, dest)}
    directions = {
            "|": {3: ('y', 1, 3), 1: ('y', -1, 1)},
            "-": {2: ('x', 1, 2), 4: ('x', -1, 4)},
            "L": {3: ('x', 1, 2), 4: ('y', -1, 1)},
            "J": {3: ('x', -1, 4), 2: ('y', -1, 1)},
            "7": {1: ('x', -1, 4), 2: ('y', 1, 3)},
            "F": {1: ('x', 1, 2), 4: ('y', 1, 3)},
    }
    
    angle = 0
    if input_lines[cur_pos.y - 1][cur_pos.x] in ["|", "7", "F"]:
        # check North
        cur_pos.y -= 1
        angle = 1
    elif input_lines[cur_pos.y + 1][cur_pos.x] in ["|", "J", "L"]:
        # check South
        cur_pos.y += 1
        angle = 3
    elif input_lines[cur_pos.y][cur_pos.x + 1] in ["-", "J", "7"]:
        # check East
        cur_pos.x += 1
        angle = 2
    elif input_lines[cur_pos.y][cur_pos.x - 1] in ["-", "L", "F"]:
        # check West
        cur_pos.x -= 1
        angle = 4
    cur_pos.angle = angle
    
    # map out the main pipe loop
    steps = 1
    cur_pipe = input_lines[cur_pos.y][cur_pos.x]
    while cur_pipe != "S":
        new_pos = cur_pos.copy()
        # print(f"{cur_pipe} @ {cur_pos} from {angle}")
        if cur_pipe == ".":
            print("LKHJASGD LIAQSKIJDGHUASLIDHlhkjgASDKLJHGASD")
            return
        
        # use directions dict to move
        source = directions[cur_pipe][angle]
        cur_pos[source[0]] += source[1]
        angle = source[2]
        new_pos.angle = angle
        
        pipe_tiles.append(new_pos)
        
        # take a step
        cur_pipe = input_lines[cur_pos.y][cur_pos.x]
        steps += 1
    print(f"{steps=}")
    # print(pipe_tiles)
    bb_path = mplPath.Path(np.array([*pipe_tiles]))
    
    top_left = Point(min([x.y for x in pipe_tiles]), min([x.x for x in pipe_tiles]))
    print(f"{top_left=}")
    bottom_right = Point(max([x.y for x in pipe_tiles]), max([x.x for x in pipe_tiles]))
    print(f"{bottom_right=}")
    top_right = Point(bottom_right.y, top_left.x)
    print(f"{top_right=}")
    bottom_left = Point(top_left.y, bottom_right.x)
    print(f"{bottom_left=}")
    bounding_area = (bottom_right.y - top_left.y+1) * (bottom_right.x - top_left.x+1)
    
    tiles_outside = 0
    tiles_inside = 0
    
    # From a given point, trace a ray that does not pass through any vertex of the
    # polygon (all rays but a finite number are convenient). Then, compute the number n
    # of intersections of the ray with an edge of the polygon. Jordan curve theorem
    # proof implies that the point is inside the polygon if and only if n is odd.
    for y in range(top_left.y, bottom_right.y+1):
        for x in range(top_left.x, bottom_right.x+1):
            pipe_type = input_lines[y][x]
            # print(f"Checking {Point(y, x)} ({pipe_type})")
            if Point(y, x) in pipe_tiles:
                # ignore tiles on the loop
                # print("\tSkipped")
                continue
            if bb_path.contains_point((y, x)):
                tiles_inside += 1
            else:
                tiles_outside += 1
            # winding = 0
            # ray = 0
            # while (rayy := y + ray) < len(input_lines) and (rayx := x + ray) < len(input_lines[rayy]):
            #     try:
            #         cross_point = Point(rayy, rayx)
            #         cross = pipe_tiles[pipe_tiles.index(cross_point)]
            #         if cross.angle == 1 or cross.angle == 4:
            #             # path is counterclockwise
            #             winding += 1
            #         elif cross.angle == 2 or cross.angle == 3:
            #             # path is clockwise
            #             winding -= 1
            #         else:
            #             print("AKLJHSGD KJAHSGD KJHAYGASKJDHGAIKLJSGHD")
            #             return
            #     except ValueError:
            #         pass
            #     ray += 1
            #
            # if winding == 0:
            #     # print("\tOutside")
            #     tiles_outside += 1
            # else:
            #     print("\tInside")
            #     tiles_inside += 1
    
    estimation = tiles - bounding_area + len(pipe_tiles) + tiles_inside + tiles_outside
    print(f"\n{tiles=}, counted={estimation}, {tiles == estimation}")
    print(f"{tiles_inside=}")
    print(f"{tiles_outside=}")
    
    # 1343 too high
    # 411 correct
