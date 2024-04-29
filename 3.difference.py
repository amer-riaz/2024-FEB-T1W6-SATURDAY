# important difference between primitive and non-primitive data types

# primitive data types
num1 = 5        # assign 5 to num1

num2 = num1     # assign the value of num1 to num2, called copy by value

num1 = 10       # change value of num1 to 10

print(num1)
print(num2)

# non-primitive data types
list1 = [1,2,3,4]       # assign [] to list1

list2 = list1           # assign list1 to list2, called copy by reference, by C language points to same memory - pointers

list3 = list1.copy()    # copy list1 to list3

list1.append(5)         # change something in list1, it changes list2 as well

print(list1)
print(list2)
print(list3)


