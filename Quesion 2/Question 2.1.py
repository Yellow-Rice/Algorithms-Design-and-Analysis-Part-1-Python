input_file = open("QuickSort.txt")
integer_array = input_file.readlines()
input_file.close()
SIZE = len(integer_array)
for i in range(SIZE):
    integer_array[i] = int(integer_array[i])


def quicksort(left, right):
    if (right - left <= 1):
        return 0

    pivot = partition(left, right)
    return right - left - 1 + quicksort(left, pivot) + quicksort(pivot + 1, right)


def partition(left, right):
    pivot = integer_array[left]
    i = left
    for j in range(left + 1, right):
        if integer_array[j] < pivot:
            i += 1
            integer_array[i], integer_array[j] = integer_array[j], integer_array[i]
    integer_array[left], integer_array[i] = integer_array[i], integer_array[left]
    return i


print quicksort(0, SIZE)