# list all numbers from 1 to 100, and state whether odd or even
# we can use range in python3
# range(10) has values 0 to 9
# range(2, 5) has values [2, 3, 4]

list_even = []
list_odd = []

for i in range(1, 101):
    # print(i)
    if (i % 2 == 0):
        list_even.append(i)
        # print(f"{i} is even")
    else:
        list_odd.append(i)
        # print(f"{i} is odd")

print(f"Even list: {list_even}")
print("\n")     # prints new line

print(f"Odd list: {list_odd}")