# Selection sort algorithm example (ascending order)
arr = []

num = int(input("Enter range: "))
for i in range(0, num):
    ele = int(input(f"Enter element {i+1}: "))
    arr.append(ele)


def sort(arr):
    for i in range(0, num-1):
        mini = arr[i]
        loc = i
        for j in range(i+1, num):
            if arr[j] < mini:
                mini = arr[j]
                loc = j

            if arr[loc] < arr[i]:
                arr[i], arr[loc] = arr[loc], arr[i]
    return arr


selection_sort = sort(arr)
print("Sorted: ", selection_sort)
