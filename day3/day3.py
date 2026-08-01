// search the correct index of an element in an array
// using linear search
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
        
        
        


// search the correct index of an element in an array
// using binary search


n = int(input("Enter the number of element: "))
arr = list(map(int, input("Enter the element: ").split()))
if len(arr) != n:
    print("enter number of correct element: ")
else:
    key = int(input("Enter searching element: "))
    
    low = 0
    high = n-1
    
    found = False
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key
            print("seaching element at index: ", mid)
            found = True
            break
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    if not found:
        print(" searching element")
            
    