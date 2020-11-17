from sys import stdin


def countSpaces(string: str):
    for i in range(0, len(string)):
        if string[i] == ' ' or string[i] == '\t':
            continue
        else:
            return i


def stringToMD(text: str):
    output = ''
    for line in text.splitlines():

        # Se è un a capo va riportato uguale
        # if line == '\n':
        #    output += line

        # Se non ci sono spazi => è un header
        if countSpaces(line) == 0:
            # An header :
            output += '## ' + line.strip() + '\n'
        else:
            if line.lstrip().startswith('-'):
                # Se è un comando
                output += '\n---\n**-**\t' + line.strip() + '\n'
            else:
                output += '\n\t' + line.strip() + '\n'

    return output


if __name__ == "__main__":
    """
    lines = []
    for line in stdin:
        lines.append(line)
    texttomd(lines)
    """
    with open("test.md") as fl:
        print(stringToMD(fl.readlines()))
