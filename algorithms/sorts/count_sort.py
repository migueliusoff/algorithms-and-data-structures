def sort(array, value_range):
    count = [0] * value_range
    for num in array:
        count[num] += 1
    array_sorted = []
    for i in range(len(count)):
        array_sorted += [i] * count[i]
    return array_sorted


if __name__ == '__main__':
    print(sort([5, 1, 3, 4, 10, 0, 25, 3], 26))
