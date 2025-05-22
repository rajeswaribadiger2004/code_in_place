"""
The user will be prompted to enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story: "At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}."
"""

def main():
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

if __name__ == "__main__":
    main()

"""
Note: the "print" function MUST be inside of the def main(): function to work!!
"""
