from main import *

if __name__ == '__main__':
    input_data = validator(space_killer(inputer()))
    if input_data is not None:
        print(calc(input_data))
    else:
        exit(0)
