import random


def addition():
    question_num_1 = random.randint(5, 20)
    question_num_2 = random.randint(5, 20)
    answer = question_num_1 + question_num_2
    ask_answer = int(input(str(question_num_1) + '+' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data


def subtraction():
    question_num_1 = random.randint(25, 50)
    question_num_2 = random.randint(1, 25)
    answer = question_num_1 - question_num_2
    ask_answer = int(input(str(question_num_1) + '-' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data

def multiply():
    question_num_1 = random.randint(5, 20)
    question_num_2 = random.randint(5, 20)
    answer = question_num_1 * question_num_2
    ask_answer = int(input(str(question_num_1) + '*' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data


def division():
    question_num_1 = random.randint(25, 50)
    question_num_2 = random.randint(1, 25)
    answer = question_num_1 / question_num_2
    ask_answer = int(input(str(question_num_1) + '/' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data

def check(data):
    rand_ans = data[0]
    user_ans = data[1]
    if rand_ans == user_ans:
        print('정답입니다.')
    else:
        print('틀렸습니다, 정답은 {0} 입니다.'.format(rand_ans))


def main():
    print('\n1) Addition')
    print('2) Subtraction')
    print('3) Multiply')
    print('4) Division\n')
    operation_ask = int(input('Enter 1 ~ 4 : '))
    if operation_ask == 1:
        check(addition())
    elif operation_ask == 2:
        check(subtraction())
    elif operation_ask == 3:
        check(multiply())
    elif operation_ask == 4:
        check(division())
    else:
        print("유효하지 않습니다. 다시 입력해주세요.\n")
        main()


main()