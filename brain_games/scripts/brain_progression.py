import prompt, random, math


def welcome_user():
    print("Welcome to the Brain Games!")


def wrong_answer(name, your_answer, true_answer):
    ins_text = "' is wrong answer ;(. Correct answer was '"
    print("'", your_answer, ins_text, true_answer, "'.", sep='')
    print("Let's try again, " + name + "!")


def true_answer_message():
    print("Correct!")


def main():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print("What number is missing in the progression?")

    round = 0
    miss_num = 0
    while round < 3:
        num1 = random.randint(1, 5)
        step = random.randint(1, 5)
        hidden = random.randint(1, 8)
        i = 0
        question = str(num1)
        while i < 10:
            num1 = num1 + step
            if int(hidden) == i:
                question = question + " .."
                miss_num = num1
            else:
                question = question + " " + str(num1)

            i += 1

        print("Question:", question)
        your_answer = int(prompt.string('Your answer: '))
        if int(your_answer) == miss_num:
            true_answer_message()
            if round == 2:
                print("Congratulations, ", name, "!", sep='')
        else:
            wrong_answer(name, your_answer, miss_num)
            break
        round += 1

if __name__ == '__main__':
    main()