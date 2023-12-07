"""

"""
from collections import Counter
from functools import total_ordering

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cards2 = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}


class Hand:
    def __init__(self, hand: str):
        self.hand: str = hand
        self.strength: int = self.get_hand_type()
    
    def get_hand_type(self) -> int:
        """
        Five of a kind -> 6
        Four of a kind -> 5
        Full house -> 4
        Three of a kind -> 3
        Two pair -> 2
        One pair -> 1
        High card -> 0
        """
        count = Counter(self.hand)
        
        match count.most_common(1)[0][1]:
            case 5:
                # five of a kind
                return 6
            case 4:
                # four of a kind
                return 5
            case 3:
                # three of a kind or full house
                if (fh := count.most_common(2)[1][1]) == 2:
                    return 4
                else:
                    # print(count.most_common(), fh)
                    return 3
            case 2:
                # two pair or one pair
                if (fh := count.most_common(2)[1][1]) == 2:
                    return 2
                else:
                    # print(count.most_common(), fh)
                    return 1
        return 0
    
    def __str__(self):
        return f"'{self.hand}'({self.strength})"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.hand == other.hand
    
    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        
        if self.strength == other.strength:
            for s, o in zip(self.hand, other.hand):
                if cards[s] < cards[o]:
                    return True
                elif cards[s] > cards[o]:
                    return False
        return False


@total_ordering
def task1(input_lines: list[str]):
    """
    
    """
    bets = []
    for line in input_lines:
        hand, bid = line.split()
        hand = Hand(hand)
        # print(hand)
        bets.append([hand, int(bid)])
    print(bets)
    
    bets.sort()
    print(bets)
    sum = 0
    for i, bet in enumerate(bets):
        sum += bet[1] * (i + 1)
    print(sum)


"""

"""


class Hand2:
    def __init__(self, hand: str):
        self.hand: str = hand
        self.jokers = self.hand.count('J')
        self.strength: int = 0
        self.strength = self.get_hand_type()
    
    def get_hand_type(self) -> int:
        """
        Five of a kind -> 6
        Four of a kind -> 5
        Full house -> 4
        Three of a kind -> 3
        Two pair -> 2
        One pair -> 1
        High card -> 0
        """
        temp_hand = self.hand.replace('J', '') + 'J' * self.jokers
        count = Counter(temp_hand)
        
        mostests = count.most_common()
        mc = mostests[0]
        match mc[1]:
            case 5:
                # AAAAA = 5 of a Kind
                print("5 of a Kind?", self)
                return 6
            case 4:
                # AAAA_ = 4 of a Kind
                smc = mostests[1]
                print("4 of a Kind?", self)
                if mc[0] == 'J':
                    # JJJJA = 5 of a Kind
                    return 6
                elif self.jokers == 1:
                    # AAAAJ = 4 of a Kind
                    return 6
                elif self.jokers > 0:
                    print(f"\t\tSOMETHINGS WRONG IN 4 {self}")
                else:
                    # AAAAB
                    return 5
            case 3:
                # AAA__
                smc = mostests[1]
                print("3 of a Kind?", self)
                if mc[0] == 'J':
                    # JJJ__
                    if smc[1] == 2:
                        # JJJAA = 5 of a Kind
                        return 6
                    else:
                        # JJJAB = 4 of a Kind
                        return 5
                elif self.jokers == 1:
                    # AAABJ = 4 of a Kind
                    return 5
                elif self.jokers == 2:
                    # AAAJJ = 5 of a Kind
                    return 6
                elif self.jokers > 0:
                    print(f"\t\tSOMETHINGS WRONG IN 3"
                          f" {self}")
                elif smc[1] == 2:
                    # AAABB = Full House
                    return 4
                else:
                    # AAABC = 3 of a Kind
                    return 3
            case 2:
                # AA___
                smc = mostests[1]
                if smc[1] == 2:
                    # AABB_ = 2 Pair
                    print("2 Pair?", self)
                    if self.jokers == 1:
                        # AABBJ = Full House
                        return 4
                    elif self.jokers == 2:
                        # AAJJB = 4 of a Kind
                        return 5
                    elif self.jokers > 0:
                        print(f"\t\tSOMETHINGS WRONG IN 2 {self}")
                    else:
                        # AABBC
                        return 2
                else:
                    # AABC_ = 1 Pair
                    print("1 Pair?", self)
                    if self.jokers == 1 or self.jokers == 2:
                        # AABCJ = JJABC = 3 of a Kind
                        return 3
                    elif self.jokers > 0:
                        print(f"\t\tSOMETHINGS WRONG IN 1 {self}")
                    else:
                        # AABCD = 1 Pair
                        return 1
        # ABCD_
        print("High Card?", self)
        if self.jokers == 1:
            # ABCDJ = 1 Pair
            return 1
        elif self.jokers > 0:
            print(f"\t\tSOMETHINGS WRONG IN 0 {self}")
        return 0
    
    def __str__(self):
        return f"'{self.hand}'({self.strength})"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return sorted(self.hand) == sorted(other.hand)
    
    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        
        if self.strength == other.strength:
            for s, o in zip(self.hand, other.hand):
                if cards2[s] < cards2[o]:
                    return True
                elif cards2[s] > cards2[o]:
                    return False
        return False


def task2(input_lines: list[str]):
    """
    
    """
    bets = []
    for line in input_lines:
        hand, bid = line.split()
        hand = Hand2(hand)
        # print(hand)
        bets.append([hand, int(bid)])
    # print(bets)
    
    bets.sort()
    print(bets)
    sum = 0
    for i, bet in enumerate(bets):
        sum += bet[1] * (i + 1)
    print(sum)
    # 255456321 is too low
    # 255661005 is too high
    # 255632664 is just right
