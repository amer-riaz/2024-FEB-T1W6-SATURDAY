# factorial

# 6! = 1 * 2 * 3 * 4 * 5 * 6;           1 times 2 times 3 ...

num = 6

fact_result = 1

for i in range(1, num+1):
    fact_result *= i

print(fact_result)