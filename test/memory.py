import sys


print(sys.getsizeof(1))
print('=' * 50)

print(sys.getsizeof(''))
print(sys.getsizeof('abc'))
print('=' * 50)

print(sys.getsizeof([]))
print(sys.getsizeof([1]))
print(sys.getsizeof([1, 2, 3]))
print('=' * 50)

print(sys.getsizeof([]))
print(sys.getsizeof(['a']))
print(sys.getsizeof(['a', 'b', 'c']))
print('=' * 50)

print(sys.getsizeof([[]]))
print(sys.getsizeof([[], [], []]))
print(sys.getsizeof([[1], [2], [3]]))
print(sys.getsizeof([[1, 2, 3], [4], [5, 6]]))
print(sys.getsizeof([[1, 2, 3], [4], [5, 6]][0][1]))
print('=' * 50)
