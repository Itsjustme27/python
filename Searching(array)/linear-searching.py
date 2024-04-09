arr = [10, 20, 30]

i = 0

try:
    item = int(input("Enter a number: "))
except ValueError:
    print("Please Enter a valid integer!")

while i < len(arr):
    if arr[i] == item:
        print("item found")
        print(f"location: {i}")
        break
    i += 1
else:
    print("Not found")


