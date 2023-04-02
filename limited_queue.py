'''Алгоритом организаванной очереди ограниченного размера.'''


from typing import Callable, Dict, Iterator, List, Optional


class MyQueueSized:
    '''
    Класс организованной очереди.
    self.head - начало очереди, self.tail - хвост очереди,
    self.max_size - максимальное размер очереди, self.size -
    размер очереди в данный момент.
    '''

    items: List[Optional[int]]
    max_size: int
    head: int
    tail: int
    size: int

    def __init__(self, max_size: int) -> None:
        '''Конструктор класса.'''
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    @property
    def is_empty(self) -> bool:
        '''Метод проверяет, что в очереди нет элементов.'''
        return self.size == 0

    def push(self, item: int) -> Optional[str]:
        '''Метод добавляет в очередь, в случае если в ней есть место.'''
        if self.size != self.max_size:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        return None

    def len_size(self) -> int:
        '''Метод возвращает количество элементов в очереди.'''
        return self.size

    def peek(self) -> Optional[int]:
        '''Метод возращает значение первого элемента очереди.'''
        if self.is_empty:
            return None
        return self.items[self.head]

    def pop(self) -> Optional[int]:
        '''
        Метод удаляет из очереди первый элемент и возвращает его значение.
        '''
        if self.is_empty:
            return None
        head_pop = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
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
    method: str
    value: List[str]
    for command in commands:
        method, *value = command.split()
        if method == 'push':
            if queue.items[queue.tail] is None:
                methods[method](*value)
            else:
                print('error')
        else:
            print(methods[method]())


if __name__ == '__main__':
    count_commands: int = int(input())
    max_size_queue: int = int(input())
    commands: Iterator[str] = (input() for _ in range(count_commands))
    working_with_a_queue(commands, max_size_queue)
