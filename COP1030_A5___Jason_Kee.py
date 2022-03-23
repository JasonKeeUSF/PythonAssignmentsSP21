##
# A5 - Jason Kee
#
## Return Name Function
def yourLastName() :
    return "Kee"
#
## m Function
def fivester(m) :
    return m*5
#
## Minecraft Age Funtion
def oldEnoughToPlayMinecraft(age) :
    MINIMUMAGE=7
    if age>=MINIMUMAGE :
        return True
    else :
        return False
#
## Main Function
def main() :
    print("Name : ", yourLastName())
    print("fivester(10) : ", fivester(10))
    print("oldEnoughToPlayMinecraft(10) : ", oldEnoughToPlayMinecraft(10))
#
## Call Main Function
if __name__=="__main__":
    main()
