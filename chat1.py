
def read_file(filename):
    data = []
    with open(filename,'r',encoding='utf-8-sig') as f:
        for i in f:
            data.append(i.strip())
    return data


def write_file(filename, lines):
    a = None
    with open(filename,'w') as f:
        for i in lines:
            if not '\u4e00' <= i <= '\u9fa5':
                a = i
                continue
            else:
                if a:
                    f.write(a + ':' + i + '\n')


def main():
    lines = read_file('input.txt')
    write_file('output.txt', lines)

main()