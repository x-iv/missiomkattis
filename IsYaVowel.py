def count_vowels(word):
    vowels_without_y = 0
    vowels_with_y = 0
    vowels = set("aeiou")

    for char in word:
        if char in vowels:
            vowels_without_y += 1
            vowels_with_y += 1
        elif char == 'y':
            vowels_with_y += 1

    return vowels_without_y, vowels_with_y

# Input
word = input().strip()

# Count vowels
count_without_y, count_with_y = count_vowels(word)

# Output
print(count_without_y, count_with_y)
