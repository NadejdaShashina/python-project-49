import prompt, random


def welcome_user():
    print("Welcome to the Brain Games!")

def wrong_answer(name, your_answer, maths):
    ins_text = "' is wrong answer ;(. Correct answer was '"
    print("'", your_answer, ins_text, maths,"'.", sep='')
    print("Let's try again, " + name + "!")

def true_answer():
    print("Correct!")
def main():

    welcome_user()
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print("What is the result of the expression?")
    ops = ['+', '-', '*']
    i = 0

    while i < 3:
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        operation = random.choice(ops)
        question = str(num1) + " " + operation + " " + str(num2)
        print("Question:", question)
        maths = eval(question)
        your_answer = int(prompt.string('Your answer: '))
        if your_answer == maths:
            true_answer()
            if i == 2:
                print("Congratulations, ", name, "!", sep='')
        else:
            wrong_answer(name, your_answer, maths)
            break
        i += 1
 
if __name__ == '__main__':

    main()