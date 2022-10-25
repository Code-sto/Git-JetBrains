import ast
import copy
import re
import sys
import os
import glob
import re

files = []
path = sys.argv[1]
if re.match(r'.*\.py', path):
    files.append(path)
else:
    for name in glob.glob(r'{}\*.py'.format(path)):
        files.append(name)




blank_counter = 0




def len_check(path, arg, num):
    if len(arg) > 79:
        print('{}: Line {}: S001 Too long'.format(path, num))


def indentation_check(path, arg, num):
    if re.match(r'^(?:\s{4})*\s{1,3}\S', arg) :
        print('{}: Line {}: S002 Indentation is not a multiple of four'.format(path, num))


def semicolon_check(path, arg, num):
    if not re.match(r'.*;', arg):
        pass
    elif not re.match(r".*'.*;'", arg) and not re.match(r'.*#.*;.*', arg):
        print('{}: Line {}: S003 Unnecessary semicolon'.format(path, num))


def spaces_comments(path, arg, num):
    if re.match(r'.*#', arg):
        if not re.match(r'.*\s{2}#', arg):
            if re.match(r'#', arg):
                pass
            else:
                print('{}: Line {}: S004 Less then two spaces before inline comments'.format(path, num))


def TODO(path, arg, num):
    if re.match(r'.*# todo.*', arg, re.IGNORECASE):
        print('{}: Line {}: S005 TODO found'.format(path, num))


def blank_lines(path, arg, num):
    global blank_counter
    if not re.match(r'.*\w', arg):
        blank_counter += 1
    else:
        if blank_counter > 2:
            print('{}: Line {}: S006 More than two blank lines used before this line'.format(path, num))
        blank_counter = 0


def spaces(path, arg, num):
    if re.match(r'class\s\s+', arg):
        print('{}: Line {}: S007 Too many spaces after "class"'.format(path, num))
    if re.match(r'\s*def\s\s+', arg):
        print('{}: Line {}: S007 Too many spaces after "def"'.format(path, num))


def camel_case(path, arg, num):
    if re.match(r'class\s\w*', arg):
        word = re.match(r'class\s\w*', arg).string.split()
        if not re.match(r'class\s*[A-Z]', arg):
            print('{}: Line {}: S008 Class name "{}" should use CamelCase'.format(path, num, word[1]))


def snake_case(path, arg, num):
    if re.match(r'\s*def\s\w*', arg):
        word = re.match(r'\s*def\s\w*', arg).string.split()
        if re.match(r'\s*def\s_?[A-Z]', arg):
            print('{}: Line {}: S009 Function name "{}" should use snake_case'.format(path, num, word[1]))


def arg_snake_case(path):
    file = open(path, 'r')
    new_file = file.read()
    tree = ast.parse(new_file)
    node = ast.walk(tree)
    arg_list = []
    arg_line_list = []
    for n in node:
        if isinstance(n, ast.arg):
            arg_list.append(n.arg)
            arg_line_list.append(n.lineno)

    for i in range(len(arg_list)):
        if re.match(r'[A-Z]', arg_list[i]):
            print('{}: Line {}: S010 Argument name "{}" should be snake_case'.format(path, arg_line_list[i], arg_list[i]))
    file.close()


def variables_snake_case(path):
    file = open(path, 'r')
    new_file = file.read()
    tree = ast.parse(new_file)
    node = ast.walk(tree)
    variables = []
    variables_line = []
    for n in node:
        if isinstance(n, ast.FunctionDef):
            for i in n.body:
                if isinstance(i, ast.Assign):
                    for j in i.targets:
                        if isinstance(j, ast.Name):
                            variables.append(j.id)
                            variables_line.append(j.lineno)

    for i in range(len(variables)):
        if re.match(r'[A-Z]*', variables[i]):
            print('{}: Line {}: S011 Variable "{}" should be snake_case'.format(path, variables_line[i], variables[i]))
    file.close()


def argument_mutable(path):
    file = open(path, 'r')
    new_file = file.read()
    tree = ast.parse(new_file)
    node = ast.walk(tree)
    for n in node:
        if isinstance(n, ast.FunctionDef):
            for i in n.args.defaults:
                if isinstance(i, ast.Constant):
                    pass
                if isinstance(i, ast.List):
                    if len(i.elts) < 1:
                        print('{}: Line {}: S012 Default argument value is mutable'.format(path, i.lineno))
    file.close()


if __name__ == '__main__':

    for i in files:
        file = open(i, 'r')
        counter = 0

        for line in file:
            counter += 1
            len_check(i, line, counter)
            indentation_check(i, line, counter)
            semicolon_check(i, line, counter)
            spaces_comments(i, line, counter)
            TODO(i, line, counter)
            blank_lines(i, line, counter)
            spaces(i, line, counter)
            camel_case(i, line, counter)
            snake_case(i, line, counter)
        blank_counter = 0


        file.close()

        arg_snake_case(i)
        variables_snake_case(i)
        argument_mutable(i)
