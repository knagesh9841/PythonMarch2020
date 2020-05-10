"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

"""

for row in range(1, 6):
    for col in range(5):
        print(row, end=" ")
    print()

"""

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

"""


for row in range(1, 6):
    for col in range(1, row + 1):
        print(row, end=" ")
    print()


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 


"""

for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

