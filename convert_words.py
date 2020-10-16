def convert_words(original, final):
    original = original.lower()
    final = final.lower()

    if original == final:
        return 1

    if len(original) != len(final):
        return 0

    if len(original) >= 33:
        letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        for letter in original:
            if letter in letters:
                letters.remove(letter)
            if len(letters) == 0:
                return 0

    dictionary = {}
    for index, letter in enumerate(final):
        if letter not in dictionary:
            dictionary[letter] = original[index]
        else:
            if dictionary[letter] != original[index]:
                return 0
    return 1


original, final = input().split()
print(convert_words(original, final))