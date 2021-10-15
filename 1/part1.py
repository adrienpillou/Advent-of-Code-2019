# answer: 3249140

def getFuelAmount(mass):
    return int(mass/3) - 2

with open("./input.txt") as f:
    x = f.readlines()

x = [int(i.strip()) for i in x]

res = 0
for mass in x:
    res += getFuelAmount(mass)

print(res)