def lastLetters(word):
    if len(word) == 2:
        return ' '.join(letter for letter in word[::-1])
    return ' '.join(letter for letter in word[len(word) - 1:len(word) - 3:-1])
