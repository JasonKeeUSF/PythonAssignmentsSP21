##
# A2 - Jason Kee
#
print("Hello!  Today, we are going to calculate the average weight of a group of Xenomorphs.")
print("")
#
## Obtain the info for the calculation ##
userInputOne = input("Please provide the weight for Xenomorph #1 (in kg): ")
xenoOne = float(userInputOne)
userInputTwo = input("Please provide the weight for Xenomorph #2 (in kg): ")
xenoTwo = float(userInputTwo)
userInputThree = input("Please provide the weight for Xenomorph #3 (in kg): ")
xenoThree = float(userInputThree)
#
## Calculate the average weight of the Xenomorphs ##
totalXeno = xenoOne + xenoTwo + xenoThree
averageXeno = totalXeno / 3
#
## Give the output ##
print("The average weight of the Xenomorphs: %-8.2f" % averageXeno, "kg")
print("")
print("Thank you.")
