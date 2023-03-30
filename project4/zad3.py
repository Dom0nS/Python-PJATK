#Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery. Funkcja przyjmuje:wiadomość – tekst do zaszyfrowania,                        klucz – liczbę o ile należy przesunąć litery w alfabecie             oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)            Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres tablicy z alfabetem oraz  problem podania klucza o dowolnej wielkości(20%).            Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).
def caesar_cipher(message, key, alphabet=None):
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    if key > len(alphabet):
        key = key % len(alphabet)
    message = message.lower()
    encrypted = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            if index + key > len(alphabet) - 1:
                encrypted += alphabet[index + key - len(alphabet)]
            else:
                encrypted += alphabet[index + key]
        else:
            encrypted += char

    return encrypted


if __name__ == '__main__':
    data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
    enc = caesar_cipher(data, 5)
    print(enc)
    enc = caesar_cipher(data, 3, ["a", "B"])
    print(enc)
