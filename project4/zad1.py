# Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i szerokość podłogi. (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)
import math


def panel_calc(length, width, panel_length, panel_width, panel_number_in_package):
    area = length * width * 1.1
    panel_area = panel_length * panel_width
    package_number = area / (panel_area * panel_number_in_package)

    return math.ceil(package_number)


if __name__ == '__main__':
    print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))
