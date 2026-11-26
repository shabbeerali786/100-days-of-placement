# 1.Find the Largest Element

n = int(input())
arr = list(map(int, input().split()))
if len(arr) != n:
  print("enter correct number")
else:
  max = arr[0]
  for i in arr:
    if i > max:
      max = i
  print("max: ", max)
  
  

# 2.Second Largest

n = int(input())
arr = list(map(int, input().split()))
if len(arr) != n:
  print("enter correct number")
else:
  max = arr[0]
  sec_max = arr[0]
  for i in arr:
    if i > max:
      sec_max = max
      max = i
    elif i > sec_max and i != max:
      sec_max = i
  if max == sec_max:
    print("no second largest")
  else:
    print("sec_max: ", sec_max)
  


# Reverse Array

n = int(input())
arr = list(map(int, input().split()))
if len(arr) != n:
  print("enter correct number")
else:
  for i in range(n-1, -1, -1):
    print(arr[i], end = " ")
    
    
# 4.Remove Duplicates

n = int(input())
arr = list(map(int, input().split()))
if len(arr) != n:
  print("enter correct number")
else:
  result = []
  for i in arr:
    if i not in result:
      result.append(i)
  print(*result)
    
    
    
    
# 5.Move Zeros

n = int(input())
arr = list(map(int, input().split()))
if len(arr) != n:
  print("enter correct number")
else:
  result = []
  for i in arr:
    if i != 0:
      result.append(i)
  zeros = n - len(result)

  for i in range(zeros):
    result.append(0)
  print(*result)
  
  
  
  








  
