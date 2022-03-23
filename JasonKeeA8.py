# COP1030 - Module A8 - Jason Kee
#
# Design, code, and test a program that defines a dictionary using the attached data file.
# The file contains the 20 countries in the world with the highest per capita income
# (according to the 2004 CIA factbook).

# Defining the Dictionary
countryDict = {};

# Open and Read Data
with open("percapita.txt", "r") as fp:
    for line in fp:
        line = line.strip()
        fields = line.split(' ')
        countryDict[fields[0]] = fields[1]

print("\n\n")

# (1) Use any of the methods shown in the chapter to output the contents of your dictionary.
print(countryDict)

# (2) Prompt the user to enter a country name, then output the per capita value associated 
# with that country name.
country = input("\n\nPlease enter the country name: ")

# Check to see if the country is in dictionary
if country in countryDict.keys() :
    print("\nCountry:", country, "\tPer Capita Value:", countryDict[country])
else:
    print("\n", country, "is not in the dictionary \n")
