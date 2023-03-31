"""Алгоритм реализазии структуры данных Дек.
Дек ограничен максимальным размером. Позволяет добавлять
и извлекать элементы с обоих концов"""

from typing import List, Optional, Union


class DequeMaximallyFilledOrEmpty(Exception):
    pass


class MyDeque:
    """Класс для хранения структуры данных Деком.
    Позволяет добавлять и извлекать элементы с обоих концов.
    """

    items: List[Optional[int]]
    max_size: int
    head: int
    tail: int
    size: int

    def __init__(self, max_size: int) -> None:
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    @property
    def is_empty(self) -> bool:
        """Проверка, что дек пуст."""
        return self.__size == 0

    @property
    def is_max(self) -> bool:
        """Проверка, что дек полон"""
        return self.__size >= self.__max_size

    def push_front(self, item: int) -> Optional[str]:
        """Добавляет элемент в начало дека.
        Принимает целочисленное значение. Если дек полный,
        выбрасывает исключение с сообщением 'error'"""
        if self.is_max:
            raise DequeMaximallyFilledOrEmpty('error')
        self.__items[self.__head - 1] = item
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def push_back(self, item: int) -> Optional[str]:
        """Добавляет элемент в конец дека.
        Принимает целочисленное значение. Если дек полный,
        выбрасывает исключение с сообщением 'error'"""
        if self.is_max:
            raise DequeMaximallyFilledOrEmpty('error')
        self.__items[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def pop_front(self) -> Union[int, str]:
        """Извлекает первый элемент дека и возращает его значение.
        Если дек пуст, выбрасывает исключение с сообщением 'error'"""
        if self.is_empty:
            raise DequeMaximallyFilledOrEmpty('error')
        x = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return x

    def pop_back(self) -> Union[int, str]:
        """Извлекает последний элемент дека и возращает его значение.
        Если дек пуст, выбрасывает исключение с сообщением 'error'"""
        if self.is_empty:
            raise DequeMaximallyFilledOrEmpty('error')
        x = self.__items[self.__tail - 1]
        self.__items[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return x


def deque(max_size: int, commands: List[str]) -> None:
    """Принимает максимальный размер дека список команд.
    В цикле перебирает команды и вызывает соответсвующий метод.
    При удалении из дека элемента печатает его значение."""
    deque: MyDeque = MyDeque(max_size)
    for command in commands:
        method, *value = command.split()  ## type: str, List[str]
        try:
            result: Union[int, str, None] = getattr(deque, method)(*value)
            if result:
                print(result)
        except DequeMaximallyFilledOrEmpty as error:
            print(error)


if __name__ == '__main__':
    count_commands: int = int(input())
    max_size: int = int(input())
    commands: List[str] = [input() for _ in range(count_commands)]
    deque(max_size, commands)
