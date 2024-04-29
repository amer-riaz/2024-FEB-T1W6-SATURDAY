# count vowels and consonants in a string
# count the number of upper case letters
# remove spaces from string without string methods

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

num_vowels = 0
num_consonants = 0
num_upper_case = 0

for character in sentence:
    if character.isupper():
        num_upper_case += 1

    if character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
        continue            # skip to next iteration in for loop

    if character.lower() in 'aeiou':             # 'a' in 'aeiou' -> true; 'f' in 'aeiou' -> false
        num_vowels += 1
    else:
        num_consonants += 1

print(f"number of vowels: {num_vowels}")
print(f"number of consonants: {num_consonants}")
print(f"number of upper case: {num_upper_case}")

sentence_without_space = ""

for character in sentence:
    if character != " ":
        sentence_without_space += character

print(sentence_without_space)