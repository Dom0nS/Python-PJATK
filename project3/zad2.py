import random

if __name__ == '__main__':
    list = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
                  "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

    print("Plan wycieczki:")
    for i in range(0,10):
        print(list.pop(random.randint(0, len(list)-1)))