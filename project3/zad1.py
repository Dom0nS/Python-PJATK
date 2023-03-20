def findMin(list):
    min = list[0]
    for i in range(0, len(list)):
        if list[i] < min:
            min = list[i]
    return min


def findMax(list):
    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    return max


if __name__ == '__main__':
    numbers = input("Podaj liczby po przecinku: ")
    numbers = numbers.split(",")
    numbers = [float(x) for x in numbers]
    max = findMax(numbers)
    min = findMin(numbers)

    print(f'Min: {min}, Max: {max}')
