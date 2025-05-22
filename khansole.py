import random

def main():
    print("Khansole Academy")
    
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    correct_answer = a + b

    print(f"What is {a} + {b}?")
    user_input = int(input("Your answer: "))

    if user_input == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

if __name__ == '__main__':
    main()
