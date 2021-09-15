
def read_file(filename):
    data = []
    with open(filename,'r',encoding='utf-8-sig') as f:
        for i in f:
            data.append(i.strip())
    return data


def write_file(filename, lines):
    a = None
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_image_count = 0
    Viki_word_count = 0
    Viki_sticker_count = 0
    Viki_image_count = 0
    with open(filename,'w') as f:
        for i in lines:
            s = i.split(' ')
            time = s[0]
            name = s[1]
            if name == 'Allen':
                if s[2] == '貼圖':
                    Allen_sticker_count += 1
                elif s[2] == '圖片':
                    Allen_image_count += 1
                else:
                    for m in s[2:]:
                        Allen_word_count += len(m)
            elif name == 'Viki':
                if s[2] == '貼圖':
                    Viki_sticker_count += 1
                elif s[2] == '圖片':
                    Viki_image_count += 1
                else:
                    for m in s[2:]:
                        Viki_word_count += len(m)
    print('Allen說了',Allen_word_count,'個字')
    print('Allen傳了',Allen_sticker_count,'個貼圖')
    print('Allen傳了',Allen_image_count,'張圖片')
    print('Viki說了',Viki_word_count,'個字')
    print('Viki傳了',Viki_sticker_count,'個貼圖')
    print('Viki傳了',Viki_image_count,'張圖片')
'''
            if not '\u4e00' <= i <= '\u9fa5':
                a = i
                continue
            else:
                if a:
                    f.write(a + ':' + i + '\n')
'''

def main():
    lines = read_file('LINE-Viki.txt')
    write_file('output2.txt', lines)

main()