import prompt, random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i=0
    while i<3:
        sym1 = random.randint(0, 100)
        print("Question:", sym1)
        your_answer = prompt.string('Your answer: ')
        if (sym1 % 2 == 0) and (your_answer != 'yes'):
            ins_text = "' is wrong answer ;(. Correct answer was 'yes'."
            print("'", your_answer, ins_text, sep='')
            print("Let's try again, " + name + "!")
            break
        elif (sym1 % 2 != 0) and (your_answer != 'no'):
            ins_text = "' is wrong answer ;(. Correct answer was 'no'."
            print("'", your_answer, ins_text, sep='')
            print("Let's try again, " + name + "!")
            break
        else:
            print("Correct!")
            if i == 2:
                print("Congratulations, ", name, "!", sep='')
        i += 1


def main():

    welcome_user()

if __name__ == '__main__':

    main()
