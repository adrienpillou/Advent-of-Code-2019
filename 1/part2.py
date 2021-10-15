# answer: 4870838


def getFuelAmount(mass):
    fuelAmount = int(mass/3) - 2
    return fuelAmount

with open("./input.txt") as f:
    x = f.readlines()

x = [int(i.strip()) for i in x]

res = 0
for mass in x:
    fuelAmount = getFuelAmount(mass)
    while ( fuelAmount > 0):
        res += fuelAmount
        fuelAmount = getFuelAmount(fuelAmount)

print("*************\n" + str(res))