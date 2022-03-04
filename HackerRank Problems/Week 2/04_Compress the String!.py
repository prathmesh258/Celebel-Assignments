#Compress the String!
s=input()
prev_i=''
count=0
for i in s :
    if i == prev_i:
        count+=1
    else:
        if prev_i!='':
            print((count+1,int(prev_i)), end=" ")
        prev_i=i
        count=0
print((count+1,int(prev_i)),end=" ")
