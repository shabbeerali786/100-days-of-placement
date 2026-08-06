s1 = input()
s2 = input()
sort1 = sorted(s1)
sort2 = sorted(s2)
if sort1 == sort2:
    print("Anagram")
else:
    print("Not Anagram")