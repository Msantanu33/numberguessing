#using random module
import random
Computernumber=random.randrange(1,101)
userinput=int(input("your guess no:--"))
if userinput > Computernumber:
    print("computer no is:--",Computernumber)
    print("guess no is higher")
elif userinput < Computernumber:
    print("computer no is:--",Computernumber)
    print("guess no is lower")
else:
    print("computer no is:--",Computernumber)
    print("congrats")

    