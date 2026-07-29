// Problem: Find Maximum Element in an Array
// Language: C, Python
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <stdio.h>
int findmax(int arr[], int n){
    int max = arr[0];
    for(int i = 1; i < n; i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}
int main() {
    int n;
    printf("Enter number of element: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter element: ");
    for(int i = 0; i < n; i++){
        scanf("%d",&arr[i]);
    }
    printf("max element in array: %d\n", findmax(arr, n));
    return 0;
}


----------------------------------------------------------------------------------------------------------------------

python

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Please enter the correct number of elements!")
else:
    maximum = arr[0]

    for i in arr:
        if i > maximum:
            maximum = i

    print("Maximum element:", maximum)