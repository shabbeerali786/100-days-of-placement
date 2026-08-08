# anagram PET 8

s1 = input()
s2 = input()
sort1 = sorted(s1)
sort2 = sorted(s2)
if sort1 == sort2:
    print("Anagram")
else:
    print("Not Anagram")
    
    
    
    
# LIST MULTIPLICATION PET 8

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



# PET 6, TRAP WATER


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





#largest number in a list 

num = list(map(int, (input().split())))

large = num[0]

for i in num:
    if large < i:
        large = i
print(large)





