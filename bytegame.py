import random


def main():
    answers = list(range(32,128))
    random.shuffle(answers)
    correct = 0
    for x in answers:
        guess = input("Correct answers : " + str(correct) + "\n" + chr(x) + " : ")
        if guess.isdigit() and int(guess) == x:
            print("Yes.")
            correct += 1
        print(x, "was the right answer.")


if __name__ == '__main__':
    main()