#!/usr/bin/env python3
import hashlib as h

def main():
    dictfile = open('dicionario.txt')
    dictlines = dictfile.readlines()

    for line in dictlines:
        word = line.strip()
        md5 = h.md5(word.encode()).hexdigest()
        if md5 == 'e8d95a51f3af4a3b134bf6bb680a213a':
            print("senha descoberta foi " + word)
            print("com md5 " + md5)
            break


if __name__ == '__main__':
    main()
