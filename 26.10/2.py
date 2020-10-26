seen = []
arr = list(input().split())
for i in arr:
    if(i in seen):
        print(i, 'YES')
    else:
        seen.append(i)
        print(i, 'NO')