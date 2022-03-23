# COP1030 - Jason Kee - Module A9
#
# Create a class called Creature. Include methods to set the creature's name, species, and weight. 
# Also include methods to get the creature's name, species, and weight. Next, design, code, and test 
# code that demonstrates your new Creature class. At minimum, your code should create (instantiate) 
# two Creature objects, and call each of the set/get methods for each of the two Creature objects. 
# Be sure to output the value of each of the items (name, species, weight) as you call their get 
# methods. Note: Your get methods should not perform output; instead, they should return info to the 
# calling code, and it's then up to the calling code to output the returned value.

# Create Creature class
class Creature:
    # Set Name, Species, Weight
    def setCreatureName(self,name):
        self.name = name
    def setCreatureSpecies(self,species):
        self.species = species
    def setCreatureWeight(self,weight):
        self.weight = weight
    # Get Name, Species, Weight
    def getCreatureName(self):
        return self.name
    def getCreatureSpecies(self):
        return self.species
    def getCreatureWeight(self):
        return self.weight

# Create two Creature objects
creature1 = Creature()
creature2 = Creature()

# Adding Values to Creature object 1
creature1.setCreatureName("Creature Name 1")
creature1.setCreatureSpecies("Creature Species 1")
creature1.setCreatureWeight("5 lbs.")

# Adding Values to Creature object 2
creature2.setCreatureName("Creature Name 2")
creature2.setCreatureSpecies("Creature Species 2")
creature2.setCreatureWeight("12 lbs.")

# Display details for Creature 1
print("Creature 1 Name: ", creature1.getCreatureName())
print("Creature 1 Species: ", creature1.getCreatureSpecies())
print("Creature 1 Weight: ", creature1.getCreatureWeight())

# Display details for Creature 2
print("\nCreature 2 Name: ", creature2.getCreatureName())
print("Creature 2 Species: ", creature2.getCreatureSpecies())
print("Creature 2 Weight: ", creature2.getCreatureWeight())


