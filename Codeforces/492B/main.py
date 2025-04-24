n, l = map(int,input().split())
lanterns = list(map(int, input().split()))
lanterns.sort()
min_radius = float(max(lanterns[0],l-lanterns[-1]))
for index, _ in enumerate(lanterns):
    if index == 0:
        continue
    radius = float(lanterns[index]-lanterns[index-1])/2
    min_radius = max(min_radius,radius)
print(min_radius)