x = float(input("Please enter your number: "))
TheSum = 0
for i in range(1, 11):
    k = 0
    for j in range(1, i + 1):
        k += j * (x ** j)
    if i % 2:
        TheSum += (1 / k)
    else:
        TheSum -= (1 / k)
print("Sum of the serie is: ", TheSum)
