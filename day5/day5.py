n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Please enter the correct number of elements!")
else:
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted Array:", arr)