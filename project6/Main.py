import MyLinkedList
import Student
import smtplib
from email.mime.text import MIMEText

filepath = "./ocenystudenci"


def emailZajety(email, students):
    for i in range(0, len(students)):
        if email == students[i]["email"]:
            return True
    return False


def wystawOcene(punkty):
    ocena = 0
    if punkty <= 50:
        ocena = 2
    if 50 < punkty <= 60:
        ocena = 3
    if 60 < punkty <= 70:
        ocena = 3.5
    if 70 < punkty <= 80:
        ocena = 4
    if 80 < punkty <= 90:
        ocena = 4.5
    if 90 < punkty <= 100:
        ocena = 5
    return str(ocena)


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def wczytajPlik(filepath):
    with open(filepath) as file:
        counter = 0
        students = {}
        for line in file:
            students_array = line.rstrip().split(",")
            students[counter] = {"email": students_array[0], "imie": students_array[1],
                                 "nazwisko": students_array[2], "punkty": students_array[3],
                                 "ocena": "", "status": ""}
            if len(students_array) >= 5 and students_array[4] in ["1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"]:
                students[counter]["ocena"] = students_array[4]
            if len(students_array) >= 6 and students_array[5] in ["GRADED", "MAILED"]:
                students[counter]["status"] = students_array[5]
            else:
                students[counter]["ocena"] = wystawOcene(int(students[counter]["punkty"]))
                students[counter]["status"] = "GRADED"
            counter += 1
        return students


def nadpiszPlik(filepath, students):
    with open(filepath, "w") as file:
        for i in range(0, len(students)):
            line = ""
            for key, value in students[i].items():
                if value != "":
                    line += str(value) + ","
            # remove last comma
            line = line[:-1]
            line += "\n"
            file.write(line)


if __name__ == '__main__':
    students = wczytajPlik(filepath)
    nadpiszPlik(filepath, students)

    while True:
        print("==============================")
        print("1. Dodaj nowego studenta")
        print("2. Usun studenta")
        print("3. Wyslij maile")
        print("4. Wyjdz")
        wybor = input("Podaj wybor: ")
        match wybor:
            case "1":
                counter = len(students)
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                while emailZajety(email, students):
                    print("Podano zajety email!")
                    email = input("Podaj email: ")
                punkty = input("Podaj punkty: ")
                ocena = wystawOcene(int(punkty))
                status = "GRADED"
                students[counter] = {"email": email, "imie": imie,
                                     "nazwisko": nazwisko, "punkty": punkty,
                                     "ocena": ocena, "status": status}
                nadpiszPlik(filepath, students)
                print(f"Dodano studenta: {students[counter]}")
            case "2":
                print(f"STUDENCI:")
                for i in range(0, len(students)):
                    print(f"Index {i}: {students[i]}")
                index = int(input("Podaj index rekordu do usuniecia: "))
                if len(students) - 1 >= int(index) >= 0:
                    del students[index]
                else:
                    print("Podano zły index")
                nadpiszPlik(filepath, students)
            case "3":
                for i in range(0, len(students)):
                    if students[i]["status"] != "MAILED":
                        subject = "Ocena z PPY"
                        body = "Ocena z PPY wynosi: " + students[i]["ocena"]
                        sender = ""  # do uzupełnienia
                        recipients = students[i]["email"]
                        password = ""  # do uzupełnienia
                        send_email(subject, body, sender, recipients, password)
                        students[i]["status"] = "MAILED"
                nadpiszPlik(filepath, students)
            case "4":
                break



