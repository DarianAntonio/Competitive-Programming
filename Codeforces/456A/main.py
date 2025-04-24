n = int(input())
laptops = []
for i in range(0,n):
    price, quality = map(int, input().split())
    laptops.append((price,quality))
laptops.sort(key = lambda x:x[1])
premise = True
for index, _ in enumerate(laptops):
    if index == 0:
        continue
    if laptops[index][0] <= laptops[index-1][0]:
        premise = False
        break
if premise:
    print("Poor Alex")
else:
    print("Happy Alex")
