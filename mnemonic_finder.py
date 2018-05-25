def main():
    for x in range(65,65+26):
        print(chr(x), x-64, x, hex(x), bin(x), x+32, hex(x+32), bin(x+32))


if __name__ == '__main__':
    main()