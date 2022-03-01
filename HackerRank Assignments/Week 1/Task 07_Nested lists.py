# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n1=[]
    s1=[]
    output=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n1.append(name)
        s1.append(score)
    p=[[v1,v2]for i1,v1 in enumerate(n1) for i2,v2 in enumerate(s1) if i1==i2 ]
    a=sorted(list(set(s1)))[1]
    for i in range(len(p)):
        if p[i][1]==a:
            output.append(p[i][0])
    output.sort()
    print(*output,sep="\n")
