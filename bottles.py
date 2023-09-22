beverage = "Lemonade"
count = 6

for count in range(6,0,-1):
   # count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)
    print("Take one down, pass it around")
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    print("")

    #print(count, "bottles of", beverage, "on the wall")
    #print(count, "bottles of", beverage)
    #print("Take one down, pass it around")
    #count = count - 1
    #print(count, "bottles of", beverage, "on the wall")
    #print("")

print("No more bottles of " + beverage + " on the wall, no more bottles of " + beverage)
print("There's nothing else to fall, because there's no more bottles of " + beverage + " on the wall.")


