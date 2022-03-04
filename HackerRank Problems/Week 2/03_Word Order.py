#Word Order
n=int(input())
dict={}
for i in range(n):
    word = input()
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(len(dict))
for key, value in dict.items():
    print(value,end=" ")
