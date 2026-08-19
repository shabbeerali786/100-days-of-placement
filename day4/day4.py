


1. # anagram PET 8

s1 = input()
s2 = input()
sort1 = sorted(s1)
sort2 = sorted(s2)
if sort1 == sort2:
    print("Anagram")
else:
    print("Not Anagram")
    
    
    
    
2. # LIST MULTIPLICATION PET 8

n1 = int(input())
l1 = list(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))
mod = 1000000007
num1 = 0
for d in l1:
    num1 = (num1*10+d)%mod
num2 = 0
for d in l2:
    num2 = (num2*10+d)%mod
print((num1*num2)%mod)



3. # PET 6, TRAP WATER


def trap(height):
    left = 0
    right = len(height) - 1
    
    left_max = 0
    right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
            
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += left_right - height[right]
            right -= 1
            
    return water
    
height = list(map(int, input().split()))
print("trapped water", trap(height))





4. #largest number in a list 

num = list(map(int, (input().split())))

large = num[0]

for i in num:
    if large < i:
        large = i
print(large)





5. #second largest number in a list

num = list(map(int, (input().split())))

large = num[0]

second_large = num[0]

for i in num:
    if large < i:
        second_large = large
        large = i
    elif i > second_large and i != large:
        second_large = i
    
if large == second_large:
    print("no second large")
else:
    print("second_large", second_large)
    
    
    
    
    
 
6. #  reverse a list

arr = list(map(int, (input().split())))
for i in range(len(arr) -1, -1, -1):
     print(arr[i], end = " ")



7. #  reverse a string

s = input()
for i in range(len(s) -1, -1, -1):
    print(s[i], end = "")           



8. # first non repeating character in a string

s = input("enter string: ")

count = {}

for i in s:
    count[i] = count.get(i, 0) + 1
for i in s:
    if count[i] == 1:
        print("first non repeating charactor: ", i)
        break
else:
    print("no non repeating charactor")
    
    
    
    
9. # first non repeating number in a list

arr = list(map(int, input().split()))   
count = {}

for i in arr:
    count[i] = count.get(i, 0) + 1
    
for i in arr:
    if count[i] == 1:
        print("first non repeating number: ", i)
        break
else:
    print("no non repeating number")
    
    
    
    
10. # remove duplicates from a array

arr = list(map(int, input().split()))
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print(*unique)



11. # remove duplicates from a string

s = input("Enter string: ")

unique = ""

for ch in s:
    if ch not in unique:
        unique += ch

print(unique)



12. # count frequency of elements in a list


arr = list(map(int, input().split()))
count = {}
for i in arr:
    count[i] = count.get(i, 0) + 1
for i in count:
    print(i, "->", count[i])
    

13. # count frequency of elements in a string

s = input("Enter string: ")

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in count:
    print(ch, "->", count[ch])
    
    
    
    
    
    
14. # check if a string is palindrome or not

s = input("Enter the string: ")

reverse = ""
for i in s:
    reverse = i + reverse
if s == reverse:
    print("palindrom")
else:
    print("Not palindrome")
    
    
    
15. # check if a number is palindrome or not

n = int(input("Enter number: "))
num = n
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse * 10 + digit
    n = n//10
if num == reverse:
    print("palindrome")
else:
    print("not palindrome")




16. # check total number vowels and consonants in a string

s = input("Enter the string: ")
vowels = 0
constant = 0
for i in s:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i.isalpha():
        constant += 1
print("vowels: ", vowels)
print("constant: ", constant)



17. # check prime number or not

n = int(input("Enter the number"))

if n < 2:
    print("Not Prime")
else:
    prime =  True

    for i in range(2, n):
        if n%i == 0:
            prime = False
            break
if prime:
    print("prime")
else:
    print("Not prime")    
    
    


18.# factorial of a number

n = int(input("Enter a number"))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print("factorial",factorial)