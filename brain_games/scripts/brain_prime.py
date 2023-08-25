import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")


def wrong_answer(name, your_answer, maths):
    ins_text = "' is wrong answer ;(. Correct answer was '"
    print("'", your_answer, ins_text , maths, "'.", sep='')
    print("Let's try again, " + name + "!")


def true_answer_message():
    print("Correct!")


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        num1 = random.randint(1, 99)
        print("Question:", num1)
        bool_true_answer = is_prime(num1)
        if ((bool_true_answer == True) and (num1 != 1)):
            true_answer = "yes"
        else:
            true_answer = "no"
        your_answer = prompt.string('Your answer: ')
        if your_answer == true_answer:
            true_answer_message()
            if i == 2:
                print("Congratulations, ", name, "!", sep='')
        else:
            wrong_answer(name, your_answer, true_answer)
            break
        i += 1


if __name__ == '__main__':
    main()