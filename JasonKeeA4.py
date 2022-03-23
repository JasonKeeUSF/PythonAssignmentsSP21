# COP1030 - Module A4 - Jason Kee
##

first = "Jason"
last = "Kee"
name = first + last
i = 0

# Loop
arr = []
for i in range(len(name)):
    inp = int(input("Please enter a number: "))
    arr.append(inp)

# Output
print("Number of numbers entered: ", len(arr))
print("Average of the numbers: ", sum(arr)/len(arr))
print("Largest Number: ", max(arr))
print("Smallest Number: ", min(arr))