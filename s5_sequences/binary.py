for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

#binary conversion
powers = []
for power in range (15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("please enter a number: "))

for power in powers:
    print(x//power)
    x %= power