n = int(input())
words = []
for i in range(0, n):
    words = words + input().split()
words = set(words)
print(len(words))