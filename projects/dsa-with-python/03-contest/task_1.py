# input - number
# return - sum of number digits

num_str = input()
sum = 0

for i in num_str:
    sum += int(i)

print(sum)