x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d = ((x2-x1)**2+(y2-y1)**2)**.5

print(f"{d:.4f}")