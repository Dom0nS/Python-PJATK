if __name__ == '__main__':

    pytania = {1: {
        "pytanie": "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
        "odpowiedzi":  ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki"]
    },
    2: {
        "pytanie":"W jakich okolicznościach czytasz książki najczęściej?",
        "odpowiedzi": ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)"]
    },
    3: {
        "pytanie":"Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
        "odpowiedzi":["chęć poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "fakt, że czytanie jest modne"]
    },
    4: {
        "pytanie":"Po książki w jakiej formie sięgasz najczęściej?",
        "odpowiedzi":["papierowej (tradycyjnej)", "e-booki (książki elektroniczne) na komputerze", "e-booki na tablecie/telefonie"]
    },
    5: {
        "pytanie":"Ile książek czytasz średnio w ciągu roku?",
        "odpowiedzi":["0", "żadnej w całości - jedynie fragmenty", "1 lub więcej"]
    },
    6: {
        "pytanie":"Jak często średnio czytasz książki?",
        "odpowiedzi":["codziennie", "raz w tygodniu", "raz w miesiącu"]
    },
    7: {
        "pytanie": "Po jakie gatunki książek sięgasz najczęściej?",
        "odpowiedzi":["kryminały/thrillery", "romanse", "psychologiczne"]
    }}

    answers = []
    correctanswer = False
    for i in pytania:
        print("pytanie: "+pytania[i]["pytanie"])
        while correctanswer != True:
            counter = 0
            for j in pytania[i]["odpowiedzi"]:
                print(chr(65+counter)+f': {j}')
                counter+= 1
            answer = input("odpowiedź: ").upper()
            match answer:
                case "A":
                    answers.append(pytania[i]["odpowiedzi"][0])
                    correctanswer = True
                case "B":
                    answers.append(pytania[i]["odpowiedzi"][1])
                    correctanswer = True
                case "C":
                    answers.append(pytania[i]["odpowiedzi"][2])
                    correctanswer = True
                case _:
                    pass
        correctanswer = False


    print("ODPOWIEDZI:\n\n")
    for k in range(1, len(answers)):
        print("pytanie: "+pytania[k]["pytanie"]+"\nodpowiedź: "+answers[k])