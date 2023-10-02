import random
Operators = ["+", "-", "*"]
Min_num = 3
Max_num = 15
total_problems = 10
points = 0
total_wrong = 0
total_asked = 0
def generate_problem():

    left = random.randint(Min_num, Max_num)
    right =random.randint(Min_num, Max_num)
    operator = random.choice(Operators)
    question = (str(left) + " " + operator + " " + str(right))
    answer = eval(question)

    return question, answer


for i in range(total_problems):
    question, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ":" + question + " = ")
        if guess == str(answer):
            points = points+1
            print("you currently have " + str(points) + " points.")
            break
        else:
            print("incorrect answer. Try again.")
            total_wrong = total_wrong + 1

total_asked = total_wrong + points
print("you got " + str(points) + "/" + str(total_asked)+ " correct.")