def mergesort(array):
    print(f"array: {array}")
    if len(array) <= 1:
        return array

    m = len(array) // 2
    print(f"m: {m}")

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    print("Merging...")
    print(f"left: {left}")
    print(f"right: {right}")

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"merged: {merged}")
    return merged


if __name__ == "__main__":
    input_list = input("Enter numbers, separated by ',': ").split(',')
    print(f"input_list: {input_list}")
    value_list = list(map(int, input_list))
    print(f"value_list: {value_list}")
    sorted_list = mergesort(value_list)
    print(sorted_list)
