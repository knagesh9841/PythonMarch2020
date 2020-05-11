# Linear Search

MyList = [5, 3, 8, 6, 7, 2]

for i in range(len(MyList)):
    if MyList[i] == 8:
        print("Element is found @Position ", i)
        break
else:
    print("Element is Not Found in List")
