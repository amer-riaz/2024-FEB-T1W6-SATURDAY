# non-primitive data types - hold/store multiple pieces of data; unlike primitive data types that can hold/store single piece of data
# list and dictionary are most used

# list - array - collection of data - indexed - mutable (individual members can be changed; members can be added/removed)
# defined using square brackets [ ]
numbers = [13, 2, 5, 98, 56]
# index     0  1  2   3   4

print(numbers)          # print whole list
print(numbers[2])       # print individual list-member

numbers[2] = 10         # change value of individual list-member
print(numbers)

numbers.append(42)      # add member at the end of the list
print(numbers)

numbers.insert(2, 16)   # add member at a specific position/index of the list
print(numbers)

numbers.pop()          # remove member at the end of the list
print(numbers)

numbers.remove(98)      # remove a member holding a specific value
print(numbers)

numbers.sort()          # sort the list in asceding order
print(numbers)

numbers.reverse()       # sort the list in descending order
print(numbers)

print(len(numbers))
print(numbers.count(2))         # count() method returns the number of times the specified element appears in the list

print("\n\n\n\n\n")     # carriage return \n, also called escape sequence

# many more functions like
# index, count

# -----------------

# tuple - collection of data - indexed - immutable (cannot be changed)
# defined using parantheses ( )

# like days of week, never need to be changed
# coordinates of a famous place/landmark

names = ("John", "Jane", "Mike", "Jane")
# index     0       1       2       3
# () - small brackets - parentheses
# {} - curly brackets - curly brackets
# [] - big brackets - square brackets

print(names)
print(names[1])

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday")
coordinates_of_some_famous_place = (123.56, 20.2)

# names[2] = "Steve" - does not work

# names.append("Steve") - does not work

print(len(names))
print(names.count("Jane"))      # count returns number of times a member exists in the tuple/list