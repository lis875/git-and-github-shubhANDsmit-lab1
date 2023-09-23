beverage = "Lemonade"

for count in range(100,1,-1):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)
    if (count%2 == 0):
        print("Take one down, pass it around")
    else:    
        print("If one of those bottles should happen to fall, " + str(count-1) + " bottles of " + beverage + " on the wall...")
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    print("")

print(count, "bottle of", beverage, "on the wall")
print(count, "bottle of", beverage)
print("If one of those bottles should happen to fall, no more bottles of " + beverage + " on the wall...")
print("")
print("No more bottles of " + beverage + " on the wall, no more bottles of " + beverage)
print("There's nothing else to fall, because there's no more bottles of " + beverage + " on the wall.")


