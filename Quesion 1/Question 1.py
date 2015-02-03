input_file = open("IntegerArray.txt")
integer_array = input_file.readlines()
input_file.close()
SIZE = len(integer_array)
MAX = 100001
for i in range(SIZE):
    integer_array[i] = int(integer_array[i])


def count_inversions(start, end):
    if end - start <= 1:
        return 0
    
    mid = (start + end) / 2
    return count_inversions(start, mid) + count_inversions(mid, end) + count_split_inversions(start, mid, end)


def count_split_inversions(start, mid, end):
    counter = 0
    
    temp_left = integer_array[start : mid]
    temp_left.append(MAX)
    temp_right = integer_array[mid : end]
    temp_right.append(MAX)
    
    i = 0
    j = 0
    for k in range(start, end):
        if temp_left[i] <= temp_right[j]:
            integer_array[k] = temp_left[i]
            i += 1
        else:
            integer_array[k] = temp_right[j]
            j += 1
            counter += mid - start - i
        
    return counter


print count_inversions(0, SIZE)