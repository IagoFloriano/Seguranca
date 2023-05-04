import hashlib as h

def main():
    dictfile = open('/usr/share/dict/brazilian')
    dictlines = dictfile.readlines()

    for line in dictlines:
        word = line.strip()
        md5 = h.md5(word.encode()).hexdigest()
        if len(word) == 5 and md5 == 'e8d95a51f3af4a3b134bf6bb680a213a':
            print(word + ": " + md5)
            break


if __name__ == '__main__':
    main()
