def main():
    for x in range(65,65+26):
        print(chr(x), x-64, x, hex(x), bin(x), x+32, hex(x+32), bin(x+32))

    for x in range(32, 127):
        if 65 <= x <= 90 or 97 <= x <= 122:
            continue
        print(chr(x), x, hex(x), bin(x))


if __name__ == '__main__':
    main()