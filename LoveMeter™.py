# OBSERVE! Though the code is in English, the *program* isn't.

from random import randint
from time import sleep
import os
from getpass import getpass


def makeName(string: str):
    # Replace all double spaces with a single space
    while "  " in string:
        string = string.replace("  ", " ")

    string = string.strip()  # Remove *unnecessary* spaces
    words = string.split(" ")
    string = ""
    for word in words:
        string += word.capitalize() + " "
    string = string[0:-1]  # Remove last space

    return string


name = input("Ditt namn: ")
name = makeName(name)  # Capitalize first letter of name(s)

crush = input("Ditt crushs namn: ")
crush = makeName(crush)  # Capitalize first letter of name(s)

sleep(1)
os.system("cls")

# Rig percentage if first name is Zach and crush's first name is Ellie.
# (It's an inside joke, okay?)
if name.split(" ")[0].lower() == "zach" and crush.split(" ")[0].lower() == "ellie":
    minPercent = -100
    maxPercent = 10
else:
    minPercent = 0
    maxPercent = 100

print(f"Detta är resultaten från 10 olika universum. Vi är nummer {randint(1, 10)}.")


sleep(1)
for i in range(10):
    print(
        f"Universum {i + 1}: {randint(minPercent, maxPercent)}% chans att {name} blir ihop med {crush}.\n"
    )
    sleep(1)

sleep(1)
# Use getpass so that potential text doesn't show; only enter closes the
# program.
getpass("\nTryck på enter för att avsluta :)")
