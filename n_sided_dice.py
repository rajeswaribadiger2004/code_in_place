import random

def main():
   dice = input("How many sides does your dice have? ")
   num = random.randint(1, int(dice))

   print("Your roll is " + str(num))
    


if __name__ == '__main__':
    main()
