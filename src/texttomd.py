from sys import stdin


def countSpaces(string: str):
    for i in range(0, len(string)):
        if string[i] == ' ' or string[i] == '\t':
            continue
        else:
            return i


def texttomd(text: str):
    output = ''
    for line in text:
        if line == '\n':
            output += line
        if countSpaces(line) == 0:
            # An header :
            output += '## ' + line.rstrip() + '\n'
        else:
            output += line.rstrip() + '\n'
    return output


if __name__ == "__main__":
    """
    lines = []
    for line in stdin:
        lines.append(line)
    texttomd(lines)
    """
    with open("test.md") as fl:
        print(texttomd(fl.readlines()))
