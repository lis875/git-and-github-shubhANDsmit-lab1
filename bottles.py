# Exercise 1 to 9:

beverage = "Lemonade"

for count in range(100,1,-1):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)
    if (count == 5):
        print("If one of those bottles should happen to fall, " + str(count-1) + " bottles of " + beverage + " on the wall...")
    else:    
        print("Take one down, pass it around")
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")
    print("")

print(count, "bottle of", beverage, "on the wall")
print(count, "bottle of", beverage)
print("Take one down, pass it around")
print("")
print("No more bottles of " + beverage + " on the wall, no more bottles of " + beverage)
print("There's nothing else to fall, because there's no more bottles of " + beverage + " on the wall.")


