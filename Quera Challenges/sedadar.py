input = input("Input the string: ")
VOWELS = 'aeiuo'


def unique_vowels(input_string: str):
    result = set()
    for s in input_string:
        if VOWELS.__contains__(s):
            result.add(s)

    return len(result)


print(unique_vowels(input))
