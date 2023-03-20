from typing import Any, Tuple

def count_operation(tanks: int, volumes: Tuple[int, ...]) -> int:
    '''
    Функция проверяет является ли элементы кортеж volumes отсортированным.
    Если нет возвращает "-1". Если да, то возвращает разницу между максимальным
    значением и минимальным. На вход принимает количество элементов в кортеже и
    сам кортеж.
    '''
    maximal: int = volumes[0]
    for i in range(1, tanks):
        if volumes[i] < maximal:
            return -1
        maximal: int = volumes[i]
    return volumes[-1] - volumes[0]


if __name__ == '__main__':
    number_of_tanks: int = int(input())
    volumes: Tuple[int, ...] = tuple(map(int, input().split()))
    print(count_operation(number_of_tanks, volumes))
