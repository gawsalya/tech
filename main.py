'''libraries required for creating script'''
import random

points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}


distribution = list("A"*9 + "B"*2 + "C"*2 + "D"*4 + "E"*12 + "F"*2 + "G"*3 + "H"*2 + "I"*9 + "J"*1 + "K"*1 + "L"*4 +
                    "M"*2 + "N"*6 + "O"*8 + "P"*2 + "Q"*1 + "R"*6 + "S"*4 + "T"*6 + "U"*4 + "V"*2 + "W"*2 + "X"*1 + "Y"*2 + "Z"*1)


def points_from_letters(word: str) -> int:
    '''calculate the number of points for the word'''
    if not isinstance(word, str):
        raise TypeError('Must be a string')
    capital_word = word.upper()
    calculate_points = 0
    for letter in capital_word:
        calculate_points += points[letter]
    return calculate_points


def assign_seven_random_tiles() -> list:
    player_tiles = []
    while len(player_tiles) < 7:
        get_random_number = random.randrange(0, 97)
        letter = distribution[get_random_number]
        player_tiles.append(letter)
        distribution.pop(get_random_number)

    return player_tiles


def return_valid_word(tiles: list) -> str:
    #random letters --> word
    #


if __name__ == "__main__":

    # score = points_from_letters("hello")
    # print(score)
    print(assign_seven_random_tiles())
    pass
