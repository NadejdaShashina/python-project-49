import prompt, random, math


def welcome_user():
    print("Welcome to the Brain Games!")


def wrong_answer(name, your_answer, true_answer):
    print("'", your_answer, "' is wrong answer ;(. Correct answer was '", true_answer, "'.", sep='')
    print("Let's try again, " + name + "!")


def true_answer_message():
    print("Correct!")


def main():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print("Find the greatest common divisor of given numbers.")
    i = 0

    while i < 3:
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        true_answer = math.gcd(num1, num2)
        question = str(num1) + " " + str(num2)
        print("Question:", question)

        your_answer = int(prompt.string('Your answer: '))
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