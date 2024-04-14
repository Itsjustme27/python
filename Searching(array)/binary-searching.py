#binary-searching
def search():
    arr = [10, 20, 30]
    lower = 0
    upper = 2
    finding = 0
    item = int(input("Enter a number: "))

    while lower <= upper:
        mid = (lower + upper) // 2

        if arr[mid] == item:
            finding = 1
            break

        if arr[mid] < item:
            lower = mid + 1
        else:
            upper = mid - 1

    if finding == 1:
        print(f"Item found at {mid}")
    else:
        print("Item not found")


search()
