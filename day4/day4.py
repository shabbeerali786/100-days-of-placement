s1 = input()
s2 = input()
sort1 = sorted(s1)
sort2 = sorted(s2)
if sort1 == sort2:
    print("Anagram")
else:
    print("Not Anagram")
    
    
    
////////////////////////////////////////

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