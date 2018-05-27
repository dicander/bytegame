import random
import time


def main():
    answers = list(range(32,127))
    random.shuffle(answers)
    correct = 0
    mistakes = []
    speeds = []
    time_before = time.time()
    confusing = {
        "0": "0 (digit)",
        "1": "1 (digit)",
        "O": "O (letter)",
        "l": "l (letter)",
    }
    for x in answers:
        before = time.time()
        to_ask = chr(x)
        if to_ask in confusing.keys():
            to_ask = confusing[to_ask]
        guess = input("Correct answers : " + str(correct) + "\n " + to_ask + " : ")
        if guess.isdigit() and int(guess) == x:
            print("Yes.")
            correct += 1
            speeds.append((time.time() - before, chr(x)))
        else:
            mistakes.append(to_ask)
        print(x, "was the right answer.")
    print(correct, "right answers out of", len(answers))
    tot_time = time.time() - time_before
    print("Total time: {:.0f}min {:.2f}s.".format(tot_time / 60, tot_time % 60))
    print("Your mistakes: ", ", ".join([chr(x) for x in mistakes]))
    print("Your results, sorted from slowest.")
    for x in reversed(sorted(speeds)):
        print("{:.2f}s : {:s}".format(x[0], x[1]))


if __name__ == '__main__':
    main()