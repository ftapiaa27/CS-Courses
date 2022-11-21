print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

planets = {
  1: 0.91,
  2: 0.38,
  3: 2.34,
  4: 1.06,
  5: 0.92,
  6: 1.19
}
# Write an if statement below:

choice = int(input("Select the number of a planet: "))
print(weight * planets.get(choice))