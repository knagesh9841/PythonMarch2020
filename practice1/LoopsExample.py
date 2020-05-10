
i = 1

while i <= 10:
    if i == 5:
        break
    elif i == 3:
        i += 1
        continue

    print(i)
    i += 1
else:
    print("While Loop Else Part Executed")


for i in range(1, 11, 2):
    print(i)
else:
    print("For Loop Else Part Executed")


for i in range(10, 0, -1):
    print(i, end=" ")           # end = "" print on same Line with Spaces


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break                   # If break is executed the else part is not executed
else:
    print("For Loop Else Part Executed")



