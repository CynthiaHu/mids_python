# score_function
def score_word(word):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    total_score = 0
    for char in word:
        if char in ('?','*'):
            score = 0
        elif char.lower() not in scores.keys():
            score = 0
        else:
            score = scores[char.lower()]
        total_score += score
    return total_score