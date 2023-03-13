if __name__ == '__main__':
    a=b=c=" Python 2023"

    print(a == b)
    print(b == c)
    print("Zmienna a typu "+str(type(a))+" o adresie "+str(hex(id(a))))
    print("Zmienna b typu "+str(type(b))+" o adresie "+str(hex(id(b))))
    print("Zmienna c typu "+str(type(c))+" o adresie "+str(hex(id(c))))

    c="Java 11"

    print(a == b)
    print(b == c)
    print("Zmienna a typu "+str(type(a))+" o adresie "+str(hex(id(a))))
    print("Zmienna b typu "+str(type(b))+" o adresie "+str(hex(id(b))))
    print("Zmienna c typu "+str(type(c))+" o adresie "+str(hex(id(c))))

