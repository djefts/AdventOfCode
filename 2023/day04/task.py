"""
The gondola takes you up. Strangely, though, the ground doesn't seem to be
coming with you; you're not climbing a mountain. As the circle of Snow
Island recedes below you, an entire new landmass suddenly appears above
you! The gondola carries you to the surface of the new island and lurches
into the station.

As you exit the gondola, the first thing you notice is that the air here is
much warmer than it was on Snow Island. It's also quite humid. Is this
where the water source is?

The next thing you notice is an Elf sitting on the floor across the station
 in what seems to be a pile of colorful square cards.

"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?"
 You ask about water sources.

"I'm not sure; I just operate the gondola lift. That does sound like
something we'd have, though - this is Island Island, after all! I bet the
gardener would know. He's on a different island, though - er, the small
kind surrounded by water, not the floating kind. We really need to come up
with a better naming scheme. Tell you what: if you can help me with
something quick, I'll let you borrow my boat and you can go visit the
gardener. I got all these scratchcards as a gift, but I can't figure
out what I've won."
"""


def task1(input_lines: list[str]):
    """
    The Elf leads you over to the pile of colorful cards. There, you discover
    dozens of scratchcards, all with their opaque covering already scratched
    off. Picking one up, it looks like each card has two lists of numbers
    separated by a vertical bar (|): a list of winning numbers and then a list
    of numbers you have. You organize the information into a table (your puzzle
    input).
    
    As far as the Elf has been able to figure out, you have to figure out which
    of the numbers you have appear in the list of winning numbers. The first
    match makes the card worth one point and each match after the first doubles
    the point value of that card.
    """
    sum = 0
    for card in input_lines:
        card_num, nums = card.split(":")
        winning_nums, my_nums = nums.split("|")
        card_num = card_num.split()[1]
        
        winning_nums = winning_nums.strip().split()
        my_nums = my_nums.strip().split()
        # print(f"{winning_nums=}, {my_nums=}")
        matches = set(winning_nums).intersection(my_nums)
        # print(f"Card {card_num} has {len(matches)} matches: {matches}.")
        
        if len(matches) >= 1:
            worth = 2 ** (len(matches) - 1)
        else:
            worth = 0
        print(f"Card {card_num} is worth {worth} points.")
        sum += worth
    print(sum)


"""
Just as you're about to report your findings to the Elf, one of you
realizes that the rules have actually been printed on the back of every
card this whole time.

There's no such thing as "points". Instead, scratchcards only cause you to
win more scratchcards equal to the number of winning numbers you have.
"""


def task2(input_lines: list[str]):
    """
    Specifically, you win copies of the scratchcards below the winning card
    equal to the number of matches. So, if card 10 were to have 5 matching
    numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

    Copies of scratchcards are scored like normal scratchcards and have the
    same card number as the card they copied. So, if you win a copy of card 10
    and it has 5 matching numbers, it would then win a copy of the same cards
    that the original card 10 won: cards 11, 12, 13, 14, and 15. This process
    repeats until none of the copies cause you to win any more cards. (Cards
    will never make you copy a card past the end of the table.)
    """
    winning_cards = [0] + [1] * (len(input_lines))
    for card in input_lines:
        card_num, nums = card.split(":")
        winning_nums, my_nums = nums.split("|")
        card_num = int(card_num.split()[1])
        # print(f"Currently own {winning_cards[card_num]} copies of Card {card_num}.")
        
        winning_nums = winning_nums.strip().split()
        my_nums = my_nums.strip().split()
        # print(f"{winning_nums=}, {my_nums=}")
        matches = set(winning_nums).intersection(my_nums)
        
        print(f"Card {card_num} has {len(matches)} matches and {winning_cards[card_num]} copies.")
        for i in range(winning_cards[card_num]):
            for j in range(len(matches)):
                # print(f"\tWon a copy of Card {card_num + j + 1}!")
                winning_cards[card_num + j + 1] += 1
    print(winning_cards)
    total_cards = sum(winning_cards)
    print(total_cards)
