'''Алгоритом организаванной очереди ограниченного размера.'''


from typing import Callable, Dict, Iterator, List, Optional


class MyQueueSized:
    '''
    Класс организованной очереди.
    self.__head - начало очереди, self.__tail - хвост очереди,
    self.__max_size - максимальное размер очереди, self.__size -
    размер очереди в данный момент.
    '''

    items: List[Optional[int]]
    max_size: int
    head: int
    tail: int
    size: int

    def __init__(self, max_size: int) -> None:
        '''Конструктор класса.'''
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    @property
    def is_not_full(self):
        '''Метод проверяет, что в очереди есть место'''
        return self.__items[self.__tail] is None

    @property
    def is_empty(self) -> bool:
        '''Метод проверяет, что очереди нет элементов.'''
        return self.__size == 0

    def push(self, item: int) -> Optional[str]:
        '''Метод добавляет в очередь, в случае если в ней есть место.'''
        if not self.is_not_full:
            return 'error'
        if self.__size != self.__max_size:
            self.__items[self.__tail] = item
            self.__tail = (self.__tail + 1) % self.__max_size
            self.__size += 1            

    def len_size(self) -> int:
        '''Метод возвращает количество элементов в очереди.'''
        return self.__size

    def peek(self) -> Union[int, str]:
        '''Метод возращает значение первого элемента очереди.'''
        if self.is_empty:
            return 'None'
        return self.__items[self.__head]

    def pop(self) -> Union[int, str]:
        '''
        Метод удаляет из очереди первый элемент и возвращает его значение.
        '''
        if self.is_empty:
            return 'None'
        head_pop = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return head_pop


def working_with_a_queue(commands: Iterator[str], max_size_queue: int) -> None:
    '''
    Функция работы с ограниченной очередью.
    Принимает итерируемый объект, содержащий комманды, и максимальный
    размер очереди.
    '''
    queue: MyQueueSized = MyQueueSized(max_size_queue)
    methods: Dict[str, Callable] = {
        'peek': queue.peek,
        'size': queue.len_size,
        'pop': queue.pop,
        'push': queue.push
    }
    for command in commands:

        method: str
        value: List[str]

        method, *value = command.split()
        result = methods[method](*value)
        if result or result == 0:
            print(result)


if __name__ == '__main__':
    count_commands: int = int(input())
    max_size_queue: int = int(input())
    commands: Iterator[str] = (input() for _ in range(count_commands))
    working_with_a_queue(commands, max_size_queue)
