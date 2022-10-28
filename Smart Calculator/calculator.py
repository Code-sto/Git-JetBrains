import sys
import re
import operator
import time
if __name__ == '__main__':
    pass
variables = {}


def check(list):
    new_list = []
    for var in list:
        if re.match(r'[A-Za-z]+', var):
            new_list.append(var)
        else:
            try:
                new_list.append(int(var))
            except ValueError:
                if re.match(r'\++', var):
                    new_list.append('+')
                elif re.match(r'-+', var):
                    if len(re.match(r'-+', var).group()) % 2 == 0:
                        new_list.append('+')
                    else:
                        new_list.append('-')
                elif re.match(r'[*/]', var):
                    new_list.append(var)
    return new_list


def plus(scratch, i):
    if isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], int):
        var = operator.add(scratch[i-1], scratch[i+1])
    elif isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], str):
        var = operator.add(int(variables[scratch[i-1]]), scratch[i+1])
    elif isinstance(scratch[i + 1], str) and isinstance(scratch[i - 1], int):
        var = operator.add(scratch[i-1], int(variables[scratch[i+1]]))
    else:
        var = operator.add(int(variables[scratch[i - 1]]),int(variables[scratch[i+1]]))
    del scratch[i - 1], scratch[i - 1], scratch[i - 1]
    scratch.insert(i - 1, var)
    return scratch


def minus(scratch, i):
    if isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], int):
        var = operator.sub(scratch[i - 1], scratch[i + 1])
    elif isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], str):
        var = operator.sub(int(variables[scratch[i - 1]]), scratch[i + 1])
    elif isinstance(scratch[i + 1], str) and isinstance(scratch[i - 1], int):
        var = operator.sub(scratch[i - 1], int(variables[scratch[i + 1]]))
    else:
        var = operator.sub(int(variables[scratch[i - 1]]), int(variables[scratch[i + 1]]))
    del scratch[i - 1], scratch[i - 1], scratch[i - 1]
    scratch.insert(i - 1, var)
    return scratch


def mul(scratch, i):
    if isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], int):
        val = operator.mul(scratch[i - 1], scratch[i + 1])
    elif isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], str):
        val = operator.mul(int(variables[scratch[i - 1]]), scratch[i + 1])
    elif isinstance(scratch[i + 1], str) and isinstance(scratch[i - 1], int):
        val = operator.mul(scratch[i - 1], int(variables[scratch[i + 1]]))
    else:
        val = operator.mul(int(variables[scratch[i - 1]]), int(variables[scratch[i + 1]]))
    del scratch[i - 1], scratch[i - 1], scratch[i - 1]
    scratch.insert(i - 1, val)
    return scratch


def divide(scratch, i):
    if isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], int):
        val = operator.floordiv(scratch[i - 1], scratch[i + 1])
    elif isinstance(scratch[i + 1], int) and isinstance(scratch[i - 1], str):
        val = operator.floordiv(int(variables[scratch[i - 1]]), scratch[i + 1])
    elif isinstance(scratch[i + 1], str) and isinstance(scratch[i - 1], int):
        val = operator.floordiv(scratch[i - 1], int(variables[scratch[i + 1]]))
    else:
        val = operator.floordiv(int(variables[scratch[i - 1]]), int(variables[scratch[i + 1]]))
    del scratch[i - 1], scratch[i - 1], scratch[i - 1]
    scratch.insert(i - 1, val)
    return scratch


def operations(list):
    total = 0
    i = 0
    while i < (len(list)):
        try:
            if list[i] == '*':
                mul(list, i)
                i = 0
            elif list[i] == '/':
                divide(list, i)
                i = 0
        except IndexError:
            print('error')
        i += 1
    j = 0
    while j < (len(list)):
        if list[j] == '-':
            minus(list, j)
            j = 0
        elif list[j] == '+':
            plus(list, j)
            j = 0
        j += 1
    if len(list) == 1:
        total = list[0]
    return total


def assign_variable(input):
    global variables
    inp = input.split()
    for i in inp:
        if i == '=':
            pass
        elif re.match(r'\w?=\d?', i):
            a = re.split(r'', re.match(r'.*=.*', i).string)
            for j in a:
                if j == '':
                    a.remove('')
            inp.remove(re.match(r'.*=.*', i).string)
            if a[0] == '=':
                inp.extend(a)
            else:
                a.extend(inp)
                inp = a
    try:
        if variables[inp[2]]:
            variables[inp[0]] = variables[inp[2]]

    except KeyError:
        variables[inp[0]] = inp[2]


def assign_old(input):
    global variables
    inp = input.split()
    for i in inp:
        if i == '=':
            pass
        elif re.match(r'\w?=\d?', i):
            a = re.split(r'', re.match(r'.*=.*', i).string)
            for j in a:
                if j == '':
                    a.remove('')
            inp.remove(re.match(r'.*=.*', i).string)
            if a[0] == '=':
                inp.extend(a)
            else:
                a.extend(inp)
                inp = a
    variables[inp[0]] = variables[inp[2]]


while True:
    inp = input()
    count_left = 0
    count_right = 0
    for i in inp:
        if i == '(':
            count_left += 1
        if i == ')':
            count_right += 1
    if count_left != count_right:
        print('Invalid expression')

    elif inp == '/exit':
        print('Bye!')
        sys.exit()
    elif inp == '/help':
        print('This is calculator, double -- counts as +, two or more + counts as one')
    elif re.match(r'/\w+', inp):
        print('Unknown command')
    elif inp == '':
        pass
    elif re.match(r'\d+[+-]+', inp):
        print('Invalid expression1')
    elif re.match(r'\d+\s\d+', inp):
        print('Invalid expression2')

    elif re.match(r'[a-zA-Z]+\d+', inp):
        print('Invalid identifier')
    elif re.match(r'\w+\s*=\s*[a-zA-Z]+\d+', inp) or re.match(r'.*=.*=', inp) \
            or re.match(r'\w+\s*=\s*\d+[a-zA-Z]+', inp):
        print('Invalid assignment')
    elif re.match(r'\s*\w+\s*=\s*\d+', inp):
        assign_variable(inp)

    elif re.fullmatch(r'\s*[a-zA-Z]+\s*', inp):
        try:
            new_var = inp.split()
            print(variables[new_var[0]])
        except KeyError:
            print('Unknown variable1')
    elif re.match(r'\s*\w+\s*=\s*\w+', inp):
        try:
            assign_old(inp)
        except KeyError:
            print('Unknown variable2')
    elif re.match(r'\d+\s*[*]{2,}', inp) or re.match(r'\d+\s*[/]{2,}', inp):
        print('Invalid expression')

    else:

        if re.match(r'.*[()]', inp):
            # if not re.match(r'.*\([\d\s+*/-]+\).*', inp):
            #     print('Invalid expression')
            #     pass
            while True:
                if ')' in inp:
                    a = re.findall(r'(\([\d\s+*/-]+)', inp)
                    for i in a:
                        i = i.replace(')', '')
                        i = i.replace('(', '')
                        _values = check(i.split())
                        new_value = operations(_values)
                        inp = inp.replace(f'({i})', str(new_value))
                else:
                    break
        text = inp.split()
        values = check(text)
        end_value = operations(values)
        print(end_value)

