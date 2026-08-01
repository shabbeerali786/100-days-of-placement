n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

if len(arr) != n:
    print("Enter the correct number of elements!")
else:
    key = int(input("Enter element to search: "))

    found = False

    for i in range(n):
        if arr[i] == key:
            print("Element found at index:", i)
            found = True
            break

    if not found:
        print("Element not found")