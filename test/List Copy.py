list1 = [0, 1, 2]
list2 = list1
list2[1] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [0, 1, 2]
list2 = list1[:]
list2[1] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [0] * 3
list1[0] = 8
print(list1)
print('-'*50)

list1 = [[0] * 3] * 5
list2 = [[0] * 5] * 3
list1[3][1] = 8
list2[1][3] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [[0 for column in range(3)] for row in range(5)]
list2 = [[0 for column in range(5)] for row in range(3)]
list1[3][1] = 8
list2[1][3] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [[0 for column in range(3)] for row in range(5)]
list2 = list1[:]
list2[3][1] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [[0 for column in range(3)] for row in range(5)]
list2 = [list1[row][:] for row in range(len(list1))]
list2[3][1] = 8
print(list1)
print(list2)
print('-'*50)

list1 = [0] * 3
list2 = [list1[:] for row in range(5)]
list1[2] = 5
list2[3][0] = 8
print(list1)
print(list2)