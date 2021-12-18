#pettyderf
'''
Usage:
    CRC.py <path> <polynom>
    CRC.py --choice <path> <choice_polynom>
    CRC.py --pol

Options:
    <choice_polynom>     Полином на выбор.
    --choice             Условие для выбора полинома.
    <polynom>            Введите полином c клавиатуры для расчета CRC.
    <path>               Путь к файлу.
    --pol                Просмотреть таблицу полиномов.
'''

abc_pol= {'CRC-5-USB':'100101','CRC-8-CCITT':'100000111','CRC-10':'11000110011','CRC-12':'1100000001111','CRC-16-CCITT':'11000000000000101','CRC-24':'1010111010110110111001011','CRC-32-IEEE':'100000100110000010001110110110111','CRC-64-ISO':'10000000000000000000000000000000000000000000000000000000000011011','CRC-64-ECMA':'10100001011110000111000011110101110101001111010100011011010010011'}

from pprint import pprint
from docopt import docopt

if __name__ == "__main__":
    args = docopt(__doc__)

class CrcFile():
    def __init__(self):
        bit = self.path()
        if args['<polynom>'] == None:
            Polynom = abc_pol[args['<choice_polynom>']]
        else:
            Polynom = args['<polynom>']
        encRem = self.Crc(bit, Polynom)
        if len(encRem) < len(Polynom) - 1:
            min = (len(Polynom) - 1) - len(encRem)
            num = '0' * min
            encRem = num + encRem
        pprint('CRC: '+encRem)

    def xor(self,a, b):
        self.a = a
        self.b = b
        if a == b :
            return '0'
        else:
            return '1'

    def Crc(self,datStr, Polynom):
        self.dataStr = datStr
        self.Polynom = Polynom
        b = len(Polynom)
        rem = ""
        temp = datStr[:b]
        while b <= len(datStr):
            if temp[0] == '1':
                div = Polynom
            else:
                div = "0" * len(Polynom)
            for i, j in zip(temp, div):
                rem += self.xor(i, j)
            t = 0
            for i in range(0, len(rem) - 1):
                if rem[i] == '0':
                    t += 1
                else:
                    break
            temp = rem[t:]
            while len(temp) < len(Polynom):
                if b <= len(datStr):
                    temp = temp + datStr[b - 1]
                    b += 1
                else:
                    break
            rem = ""
        return temp[:-1]

    def path(self):
        filename = args['<path>']
        file = open(filename, 'rb')
        bite = file.read()
        bit = ''
        for i in bite:
            one_bite = str(bin(i))
            one_bite = one_bite[2:]
            if len(one_bite) < 8:
               one_bite += '0' * (8 - len(one_bite))
            bit += one_bite
        return bit

if args['--pol']:
    pprint(abc_pol)
else:
    CrcFile()
