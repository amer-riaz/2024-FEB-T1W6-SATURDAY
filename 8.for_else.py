# for else

for i in range(10):
    print(i)
    if (i == 7):
        break
else:       # similar to break in while loop, else is executed if break is not called in a for loop; so else part of for loop executes after running the main part of for loop
    print("loop finished without interruption")