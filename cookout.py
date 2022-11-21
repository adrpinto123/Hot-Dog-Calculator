import math

pcount = int(input("How many people will be attending the cookout?: "))
hdcount = int(input("What is the max amount of hot dogs that will be given, per person?: "))
print()

WEINERS = 10
BUNS = 8

while pcount <= 0 or hdcount <= 0:

    print("Quantities entered mus be greater than 0.\n")

    pcount = int(input("How many people will be attending the cookout?: "))
    hdcount = int(input("What is the max amount of hot dogs that will be given, per person?: "))
    print()

totalhd = pcount * hdcount

#calculates minimum weiner/bun packages
minweiners = math.ceil(totalhd / WEINERS)
minbuns = math.ceil(totalhd / BUNS)

print("The minimum number of packages of hot dogs required are:", minweiners)
print("The minimum number of packages of buns required are:", minbuns)

    

#calculates left over weiner/bun packages
leftweiners = totalhd % WEINERS
leftbuns = totalhd % BUNS

if leftweiners != 0:
    print("Left over hot dog weieners:", leftweiners)
else:
    print("No left over hot dog weiners.")
if leftbuns != 0:          
    print("Left over hot dog buns:", leftbuns)
else:
    print("No left over hot dog buns")







