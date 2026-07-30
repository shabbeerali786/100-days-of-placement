// second largest element

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Please enter the correct number of elements!")
else:
    largest = arr[0]
    second_largest = arr[0]

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if largest == second_largest:
        print("No second largest element.")
    else:
        print("Second Largest Element:", second_largest)
        
        
        
    
    
// reverse a array

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Please enter the correct number of elements!")
else:
    print("Reversed Array:")

    for i in range(n - 1, -1, -1):
        print(arr[i], end=" ")