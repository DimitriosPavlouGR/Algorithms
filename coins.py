# Askisi 1
x = 99

coins = [25,10,5,1]
res = [0, 0, 0, 0]

i = 0
while x != 0:
    if (coins[i] <= x):
        res[i] += 1
        x -= coins[i]
    else:
        i += 1
print(res)
