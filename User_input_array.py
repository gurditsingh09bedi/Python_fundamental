import numpy as np
arr1 =[]
x = int(input("Enter the size of array ="))
for i in range(x):
    num = int(input("Enter the array number ="))
    arr1.append(num)
res1 = np.array(arr1)
print(res1)

arr2 = []
y = int(input("Enter the size of array ="))
for i in range(y):
    num1 = int(input("Enter the array number ="))
    arr2.append(num1)
res2 = np.array(arr2)
print(res2)

addition = res1 + res2
print("addition for array = ", addition)






