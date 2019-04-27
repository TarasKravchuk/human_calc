import inflect
import pytest

p = inflect.engine()
action_list = ["*", "+", "/", "-"]
action_dict = {"+": "plus",
               "*": "multiplication",
               "/": "division",
               "-": "minus"}

def calc(arg1, action, arg2):
    if action == action_list[0]:
        result = arg1 * arg2
    elif action == action_list[1]:
        result = arg1 + arg2
    elif action == action_list[2]:
        result = arg1 / arg2
    elif action == action_list[3]:
        result = arg1 - arg2

    return print(p.number_to_words(arg1), action_dict.get(action), p.number_to_words(arg2), " equally",
                 p.number_to_words(result))


def inputer():
    arg1 = input("please input first argument, it should be integer ")
    action = input('please input your action it can be "*" or "+" or "/" or "-" ')
    arg2 = input("please input second argument, it should be int or integer ")
    return space_killer(arg1, action, arg2)


def space_killer(*args):
    space_killer_list = []
    for arg in args:
        arg = arg.replace(' ', '')
        space_killer_list.append(arg)
    return validator(space_killer_list[0], space_killer_list[1], space_killer_list[2])


def validator(arg1, action, arg2):
    try:
        arg1 = int(arg1)
    except ValueError:
        print(f"Invalid input {arg1}, please try again ")
        return inputer()

    try:
        arg2 = int(arg2)
    except ValueError:
        print(f"Invalid input {arg2}, please try again  ")
        return inputer()

    if action not in action_list:
        print(f"Invalid input {action}, please try again ")
        return inputer()

    else:
        return calc(arg1, action, arg2)


inputer()
