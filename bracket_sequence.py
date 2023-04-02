'''Алгоритм определения правильности скобочной последовательности.'''


class Stack:
    def __init__(self) -> None:
        self.items: list = []

    def push(self, item: str):
        self.items.append(item)

    def pop(self):
        self.items.pop()


def is_correct_bracket_seq(subsequence: str) -> bool:
    '''
    Функция перебирает принятую строку.
    При нахождении открывающей скобки добавляет в стэк,
    при нахождении закрывающей, проверяет в стэке последнюю скобку,
    являются ли они парой. Если по окончании работы цикла с стэке
    не осталось скобок, вернет True.
    '''
    stack: Stack = Stack()
    for bracket in subsequence:
        if bracket in ('(', ')', '[', ']', '{', '}'):
            if bracket in ('(', '[', '{'):
                stack.push(bracket)
            elif stack.items and (
                stack.items[-1] == '(' and bracket == ')' or
                stack.items[-1] == '[' and bracket == ']' or
                stack.items[-1] == '{' and bracket == '}'
            ):
                stack.pop()
            else:
                return False
    return False if stack.items else True


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
