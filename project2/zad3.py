import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
# Pobieranie danych z ankiety
    url = 'https://www.webankieta.pl/wzor-ankiety/ankieta-czytelnicza/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(response.content)
    # Wyświetlanie pytań i możliwych odpowiedzi
    questions = soup.find_all('h2', class_='showRequired question-title')
    for index, question in enumerate(questions):
        print(f"Pytanie {index + 1}: {question.text}")
        # choices = question.parent.find_all('label')
        # for i, choice in enumerate(choices):
        #     print(f"   {chr(97 + i)}) {choice.text}")
        #
        # # Pobieranie odpowiedzi od użytkownika
        # answer = input("Wybierz odpowiedź (a, b, c, d): ")
        # print(f"Odpowiedź na pytanie {index + 1}: {choices[ord(answer) - 97].text}\n")