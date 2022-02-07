
array = input('input your list with using space:').split()
A = set(input('Enter set A:').split())
B = set(input('set B:').split())

happiness = 0
# print(sum((i in A) - (i in B) for i in array))

for item in array:
    for i in A:
        if i == item:
            happiness += 1
    for j in B:
        if j == item:
            happiness -= 1

print(happiness)



