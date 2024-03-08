'''
Name: Wyatt Fulton
Lab time: Thur 2:00 PM
'''

def food_input():
    user_num=[]
    user_string=[]
    user_input = input()
    user_input = user_input.split()
    user_string.append(user_input[0])
    user_num.append(user_input[1])
    front = 'Eating '
    back = ' a day keeps you happy and healthy.'
    accumulator = 0

    while 'quit' not in user_string:
        user_input = input()
        user_input = user_input.split()
        user_string.append(user_input[0])
        user_num.append(user_input[1])
        accumulator += 1
    for i in range(0,accumulator,1):
        print(front+user_num[i]+' '+user_string[i]+back)
  


if __name__ == "__main__":
    food_input()
