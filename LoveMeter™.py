from random import randint
from time import sleep
import os
from getpass import getpass

print("LoveMeter™ is booting up . . .")
sleep(randint(2, 5) / 2)

print("DEFAULT LANG.: SWE")
sleep(randint(1, 10) / 5)

os.system("cls")

namn = input("Ditt namn: ")
sleep(1)

crush = input("Ditt crush namn: ")
sleep(1)

os.system("cls")

print(f"Detta är resultaren från 10 olika universum. Vi är nummer {randint(1, 10)}.")
if namn.lower() == "zach" and crush.lower() == "ellie":
    minPercent = -100
    maxPercent = 10

else:
    minPercent = 0
    maxPercent = 100

for i in range(10):
    print(
        f"Universum {i + 1}: Det är {randint(minPercent,maxPercent)}% chans att {namn} blir ihop.\n"
    )
    sleep(1)

sleep(3)
getpass("\nTryck på enter för att avsluta :)")
