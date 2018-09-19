import random
import time


def main():
    """This program runs a game that asks the user for ascii codes"""
    answers, confusing, correct, mistakes, speeds, time_before = \
        generate_questions()
    correct = run_game(answers, confusing, correct, mistakes, speeds)
    print(correct, "right answers out of", len(answers))
    tot_time = time.time() - time_before
    print("Total time: {:.0f}min {:.2f}s.".format(tot_time / 60, tot_time % 60))
    print("Your mistakes:")
    for current in mistakes:
        print(current)
    print("Your results, sorted from slowest.")
    for element in reversed(sorted(speeds)):
        print("{:.2f}s : {:s}".format(element[0], element[1]))


def run_game(answers, confusing, correct, mistakes, speeds):
    """Ask the questions, return number of answers. Modifies mistakes and speeds."""
    for number in answers[:10]:
        before = time.time()
        to_ask = chr(number)
        if to_ask in confusing.keys():
            to_ask = confusing[to_ask]
        guess = input("Correct answers : " + str(correct) + "\n " + to_ask + " : ")
        if guess.isdigit() and int(guess) == number:
            print("Yes.")
            correct += 1
            speeds.append((time.time() - before, chr(number)))
        else:
            mistakes.append(to_ask + " was " + str(number) + " not " + guess + ".")
        print(number, "was the right answer.")
    return correct


def generate_questions():
    """Generates all data related to a game."""
    answers = list(range(32, 127))
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
    return answers, confusing, correct, mistakes, speeds, time_before


if __name__ == '__main__':
    main()