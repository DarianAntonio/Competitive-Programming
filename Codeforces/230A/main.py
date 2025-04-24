strength, n = map(int, input().split()) 
dragons = []
for dragon in range(0,n):
    drake_strength , strength_bonus = map(int, input().split()) 
    dragons.append((drake_strength,strength_bonus))
dragons.sort()
solvable = True
for drake in dragons:
    if strength > drake[0]:
        strength+=drake[1]
    else: 
        solvable = False
        break
if solvable:
    print("YES")
else:
    print("NO")