#ginortS
s = input()
upper_case,lower_case,odd,even=[],[],[],[]

for char in s:
    if char.isnumeric():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)
    else:
        if char.isupper():
            upper_case.append(char)
        else:
            lower_case.append(char)

print(''.join(sorted(lower_case))+''.join(sorted(upper_case))+''.join(sorted(odd))+''.join(sorted(even)))
