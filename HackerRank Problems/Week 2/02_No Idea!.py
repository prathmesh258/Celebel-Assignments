#No Idea!

n,m=[int(_) for _ in input().split()]
arr=[int(_) for _ in input().split()]
a=set([int(_) for _ in input().split()])
b=set([int(_) for _ in input().split()])
happiness=0
for i in arr:
    if i in a:
        happiness+=1 
    elif i in b:
        happiness-=1 
    else:
        happiness+=0
print(happiness)
