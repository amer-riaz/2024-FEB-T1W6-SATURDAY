# palindrome: string reversed is also the same as the original string

# firestruck = kcurterif -> not a palindrome
# racecar = racecar -> palindrome

# original_string = "firetruck"
original_string = "racecar"

reversed_string = ""

for character in original_string:
    reversed_string = character + reversed_string

print(reversed_string)

if (reversed_string == original_string):
    print("a palindrome")
else:
    print("not a palindrome")

# since above is simple if-else, it can be written using ternary operator
print("a palindrome") if (reversed_string == original_string) else print("not a palindrome")


# in python3: name = "simon", name[::-1] -> "nomis"
# name[2] -> 'm'
# name[2:4] -> 'mo'
# name[1:4] -> 'imo'
# name[4:1:-1] -> 'nom'; -1 to reverse the string
# name[::] -> 'simon';  without index value :: means first to last character
# name[::-1] -> 'nomis'