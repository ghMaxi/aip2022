import math_requests


def check_command_sum(command):
    split_command = command.split('+')
    if len(split_command) == 2 and\
       split_command[0] and split_command[1]:
        return math_requests.make_sum(
            float(split_command[0]), float(split_command[1]))
    else:
        return None


def check_command_mult(command):
    split_command = command.split('*')
    if len(split_command) == 2 and split_command[0] and split_command[1]:
        return math_requests.make_mult(
            float(split_command[0]), float(split_command[1]))
    else:
        return None


def check_command_sinus(command):
    if command[:4] == 'sin(' and command[-1]==")":
        return math_requests.make_sinus(float(command[4:-1]))
    else:
        return None


def check_factorial(command):
    if command[-1] == '!':
        return math_requests.factorial(float(command[:-1]))
    else:
        return None


def process_command(command):
    result = (check_command_sum(command) or
              check_command_mult(command) or
              check_command_sinus(command) or
              check_factorial(command))
    if result:
        print(result)


if __name__ == '__main__':
    command = input()
    while command != "exit":
        process_command(command)
        command = input()
