import random


def main():
    answers = list(range(32,127))
    random.shuffle(answers)
    correct = 0
    mistakes = []
    for x in answers:
        guess = input("Correct answers : " + str(correct) + "\n" + chr(x) + " : ")
        if guess.isdigit() and int(guess) == x:
            print("Yes.")
            correct += 1
        else:
            mistakes.append(x)
        print(x, "was the right answer.")
    print(correct, "right answers out of", len(answers))
    print("Your mistakes: ", " ".join([chr(x) for x in mistakes]))


if __name__ == '__main__':
    main()