arr = []
n = int(input("Enter range: "))
for i in range(0, n):
    num = int(input(f"Enter element {i+1}: "))  # Don't forget to press Enter after input each element
    arr.append(num)


def sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


bubble_sort = sort(arr)
print("Sorted: ", bubble_sort)
