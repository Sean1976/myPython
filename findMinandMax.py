L = [7, 1]
max = L[0]
min = L[0]
len=len(L)
for i in range(1,len):
    if L[i] > max:
        max = L[i]
    if L[i] < min:
        min = L[i]
print(min, max)