import inflect
p = inflect.engine()
action_list = ["*", "+", "/", "-"]
action_dict = {"+": "plus",
               "*": "multiplication",
               "/": "division",
               "-": "minus"}

def calc (validator_result):
    arg1 = validator_result[0]
    action = validator_result[1]
    arg2 = validator_result[2]
    if action == action_list[0]:
        result = arg1 * arg2
    elif action == action_list[1]:
        result = arg1 + arg2
    elif action == action_list[2]:
        result = arg1/arg2
    elif action == action_list[3]:
        result = arg1 - arg2
    final_result = p.number_to_words(arg1)+ " " + action_dict.get(action) + " " + p.number_to_words(arg2) + " equally" + \
                   " " + p.number_to_words(result)
    return final_result

def inputer ():
    arg1 = input("please input first argument, it should be integer ")
    action = input('please input your action it can be "*" or "+" or "/" or "-" ')
    arg2 = input("please input second argument, it should be int or integer ")
    return [arg1, action, arg2]

def space_killer (inputer_list):
    space_killer_list = []
    for arg in inputer_list:
        arg = arg.replace(' ', '')
        space_killer_list.append(arg)
    return space_killer_list

def validator (space_killer_list):
    try:
        arg1 = int(space_killer_list[0])
    except ValueError:
        print(f"Invalid input {space_killer_list[0]}, please try again ")
        return None

    try:
        arg2 = int(space_killer_list[2])
    except ValueError:
        print(f"Invalid input {space_killer_list[2]}, please try again  ")
        return None

    if not space_killer_list[1] in action_list:
        print(f"Invalid input {space_killer_list[1]}, please try again ")
        return None

    else:
        action = space_killer_list[1]
        return [arg1, action, arg2]
