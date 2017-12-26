"""
Script to handle the scoreboard output box

Taken from https://stackoverflow.com/
questions/20756516/python-create-a-text-border-with-dynamic-size
"""



def breakLine(text, wrap=80):
    if len(text) > wrap:
        char = wrap
        while char > 0 and text[char] != ' ':
            char -= 1
        if char:
            text = [text[:char]] + breakLine(text[char + 1:], wrap)
        else:
            text = [text[:wrap - 1] + '-'] + breakLine(text[wrap - 1:], wrap)
        return text
    else:
        return [cleanLine(text)]

def cleanLine(text):
    if text[-1] == ' ':
        text = text[:-1]
    if text[0] == ' ':
        text = text[1:]
    return text

def boxPrint(text, wrap=0):
    line_style = '-'
    paragraph = text.split('\n')
    if wrap>0:
        index = 0
        while index < len(paragraph):
            paragraph[index] = cleanLine(paragraph[index])
            if len(paragraph[index]) > wrap:
                paragraph = paragraph[:index] + breakLine(paragraph[index]\
                    , wrap) + paragraph[index + 1:]
            index += 1

    length = (max([len(line) for line in paragraph]))
    print('+' + line_style * length + '+')
    for line in paragraph:
        print('|' + line + ' ' * (length - len(line)) + '|')
    print('+' + line_style * length + '+')
