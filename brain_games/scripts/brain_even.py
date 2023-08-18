import prompt, random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello,"+name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sym1 = random.randint()
    print("Question:", sym1)
    your_answer = prompt.string('Your answer: ')
    i=0
    while i<3:
        if (sym1 % 2 == 0) and (your_answer == 'no'):
            print("'", your_answer, "' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, Bill!")
            break
        elif (sym1 % 2 != 0) and (your_answer == 'yes'):
            print("'", your_answer, "' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, Bill!")
            break
        else:
            print("Correct!")

        print("Congratulations, ",  name, "!", sep='')
def main():

    # greet()
    welcome_user()

if __name__ == '__main__':

    main()