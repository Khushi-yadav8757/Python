#Count Vowels in String
s = input()
v = "aeiouAEIOU"
count = 0
for i in s:
    if i in v:
        count += 1
    
print(count)
