"""
You're still riding a camel across Desert Island when you spot a sandstorm quickly
approaching. When you turn to warn the Elf, she disappears before your eyes! To be
fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents
(your puzzle input) about how to navigate the desert. At least, you're pretty sure
that's what they are; one of the documents contains a list of left/right instructions,
and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network.
Perhaps if you have the camel follow the same instructions, you can escape the haunted
wasteland!
"""
import re


class Node:
    def __init__(self, name, l, r):
        self.name = name
        self.left = l
        self.right = r
        
    def __str__(self):
        return f"{self.name}-{self.left}|{self.right}"
    
    def __repr__(self):
        return str(self)


def task1(input_lines: list[str]):
    """
    Starting with AAA, you need to look up the next element based on the next
    left/right instruction in your input. In this example, start with AAA and go right
    (R) by choosing the right element of AAA, CCC. Then, L means to choose the left
    element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2
    steps.

    Of course, you might not find ZZZ right away. If you run out of left/right
    instructions, repeat the whole sequence of instructions as necessary: RL really
    means RLRLRLRLRLRLRLRL... and so on.
    """
    directions = input_lines[0]
    
    nodes = {}
    for line in input_lines[2:]:
        reggy = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line).groups()
        nodes[reggy[0]] = Node(reggy[0], reggy[1], reggy[2])
    
    steps = 0
    cur_node = nodes["AAA"]
    dir_num = 0
    while cur_node.name != "ZZZ":
        if dir_num >= len(directions):
            dir_num = 0
        if directions[dir_num] == 'L':
            cur_node = nodes[cur_node.left]
        elif directions[dir_num] == 'R':
            cur_node = nodes[cur_node.right]
        # print(f"{cur_node}")
        dir_num += 1
        steps += 1
    print(f"Steps: {steps}")


"""
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had
the camel follow the instructions, but you've barely left your starting position. It's
going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound
by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the
number of nodes with names ending in A is equal to the number ending in Z! If you were
a ghost, you'd probably just start at every node that ends with A and follow all of the
paths at the same time until they all simultaneously end up at nodes that end with Z.
"""


def task2(input_lines: list[str]):
    """
    Here, there are two starting nodes, 11A and 22A (because they both end with A). As
    you follow each left/right instruction, use that instruction to simultaneously
    navigate away from both nodes you're currently on. Repeat this process until all of
    the nodes you're currently on end with Z. (If only some of the nodes you're on end
    with Z, they act like any other node and you continue as normal.)
    """
    directions = input_lines[0]
    
    nodes = {}
    cur_nodes: list[Node] = []
    for line in input_lines[2:]:
        reggy = re.match(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", line).groups()
        newbie = Node(reggy[0], reggy[1], reggy[2])
        nodes[reggy[0]] = newbie
        if newbie.name[-1] == 'A':
            cur_nodes.append(newbie)
    
    steps = []
    print(f"{[n.name for n in cur_nodes]}")
    for node in cur_nodes:
        step = 0
        cur_node = node
        dir_num = 0
        stop = False
        print(f"Pathing node {node}...")
        while cur_node.name[-1] != "Z":
            if dir_num >= len(directions):
                dir_num = 0
            if directions[dir_num] == 'L':
                # print("L", end='')
                cur_node = nodes[cur_node.left]
            elif directions[dir_num] == 'R':
                # print("R", end='')
                cur_node = nodes[cur_node.right]
            if step % 100 == 0:
                # print()
                pass
            # print(f"{cur_node}")
            dir_num += 1
            step += 1
        print(f"Path was  {step} steps long.")
        steps.append(step)
    print(f"Steps: {steps}")
    from math import gcd
    lcm = 1
    for i in steps:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)
