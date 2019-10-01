import re

search_repeated = re.compile(r'(\d)(?=\d\1)')
template_code = re.compile(r'[1-9]{6}')


def validate_code(value):
    if not re.match(template_code, value):
        return False
    if re.findall(search_repeated, value):
        return False
    return True


if __name__ == '__main__':
    code = ''
    while code != 'q':
        code = input("Show me the code, or enter 'q' to quit: ")
        if validate_code(code):
            print('The %s code is valid.' % code)
        else:
            print('The %s code is not valid.' % code)
