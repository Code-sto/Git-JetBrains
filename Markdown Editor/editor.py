# write your code here

# print('''# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# - Imagine
# - Norwegian Wood
# - Come Together
# - In my life
# - ~~Hey Jude~~ (that was *McCartney*)''')

formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
Final_text = ''


def help_():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def done():
    global Final_text
    file = open('output.md', 'w+')
    file.write(Final_text)
    file.close()


def plain():
    text = input("Text: ")
    global Final_text
    Final_text += text


def bold():
    text = input("Text: ")
    global Final_text
    temp = "**" + text + "**"
    Final_text += temp


def italic():
    text = input("Text: ")
    global Final_text
    temp = "*" + text + "*"
    Final_text += temp


def header():
    global Final_text
    level = int(input("Level: "))
    if level not in range(7):
        print("The level should be within the range of 1 to 6")
        header()
    else:
        text = input("Text: ")
        if Final_text == '':
            Final_text += level * "#" + " " + text + '\n'
        else:
            Final_text += '\n' + level * "#" + " " + text + '\n'


def link():
    global Final_text
    label = input("Label: ")
    url = input("URL: ")
    Final_text += "[" + label + "]" + "(" + url + ")"


def inline_code():
    global Final_text
    text = input("Text: ")
    temp = '`' + text + '`'
    Final_text += temp


def new_line():
    global Final_text
    Final_text += '\n'


def lists(chose):
    global Final_text
    rows = input('Number of rows: ')
    a = []
    if int(rows) < 1:
        print('The number of rows should be greater than zero')
        lists(chose)
    for i in range(int(rows)):
        a.append(input('Row #{0}: '.format(i + 1)))
        if chose == 'ordered-list':
            Final_text += '{0}. {1}\n'.format(i + 1, a[i])
        elif chose == 'unordered-list':
            Final_text += '* {1}\n'.format(i + 1, a[i])


def start():
    inp = input('Choose a formatter:')
    if inp in formatters:
        if inp == 'plain':
            plain()
            print(Final_text)
            start()
        elif inp == 'bold':
            bold()
            print(Final_text)
            start()
        elif inp == 'italic':
            italic()
            print(Final_text)
            start()
        elif inp == 'inline-code':
            inline_code()
            print(Final_text)
            start()
        elif inp == 'link':
            link()
            print(Final_text)
            start()
        elif inp == 'header':
            header()
            print(Final_text)
            start()
        elif inp == 'new-line':
            new_line()
            print(Final_text)
            start()
        elif inp == 'ordered-list' or inp == 'unordered-list':
            lists(inp)
            print(Final_text)
            start()
    elif inp == '!help':
        help_()
        start()
    elif inp == '!done':
        done()
    else:
        print('Unknown formatting type or command')
        start()


start()
