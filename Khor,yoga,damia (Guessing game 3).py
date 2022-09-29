import random

def main():
    """Start a element guessing game."""
    print (" Guess the element!!!")

    Elements_of_periodic_table = [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Berrylium",
        "Nitrogen",
        "Oxygen",
        "Sodium",
        "Magnesium",
        "Aluminum",
        "Silicon",
        "Sulphur",
        "Carbon",
        "Chlorine",
        "Iron",
        "Calcium",
        "Potassium",
        "Titanium",
        "Copper",
        "Zinc",
        "Silver",
        "Tin",
        "Iodine",
        "Platinum",
        "Gold",
        "Mercury",
        "Lead",
        "Boron"
        ]

    

    x = random.choice(Elements_of_periodic_table)

    guess= None

    while x != guess:


        guess = str(input("What element am I thinking of?"))

        if x == guess:
            print("You guessed {}.Congratulations you got it right !!!".format(guess))
            break
        else:
            print("You guessed {}.Unfortunetly you got the wrong answer.Please try again !".format (guess))

main()       

       

        

    
