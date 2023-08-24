#!/usr/bin/python3
import sys

# print(sys.argv[1])

with open(f'{sys.argv[1]}.txt', 'w', encoding='utf-8') as niko_text:
    niko_text.write('Wee endelea tu')
    
# print('Niko hata tu!')

if __name__ == '__main__':
    # code execution goes here
    pass