arr = []

n = int(input("Enter range: "))

for i in range(0, n):
    ele = int(input(f"Enter element {i+1}: "))
    arr.append(ele)


def sort(arr):
    for i in range(1, n):
        j = i
        while j >= 1:
            if arr[j-1] > arr[j]:  # if arr[j-1] < arr[j] for descending
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


insertionSort = sort(arr)
print("Sorted: ", insertionSort)