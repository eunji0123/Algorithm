i = tri = run = 0
inp = int(input())
c = [0] * 12

while i < 6:
    c[inp % 10] += 1
    inp //= 10
    i += 1

i = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")
