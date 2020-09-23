def balance(string):
    stack = []
    open_char = ['(', '[', '{', '<']
    close_char = [')', ']', '}', '>']
    if not string:
        return 'Insira uma palavra'
    for char in string:
        if char in open_char:
            stack.append(char)
        elif char in close_char:
            current = stack.pop()
            if current == '(':
                if char != ")":
                    return 'Não balanceado'
            if current == '{':
                if char != "}":
                    return 'Não balanceado'
            if current == '[':
                if char != "]":
                    return 'Não balanceado'
            if current == '<':
                if char != ">":
                    return 'Não balanceado'
        else:
            return 'Palavra inválida para a linguagem'
    if not stack:
        return 'Balanceado'
    else:
        return 'Não balanceado'


if __name__ == '__main__':
    bol = 'true'
    while bol:
        print('\nEscreva uma palavra no alfabeto: <{[()]}>')
        r = input().replace(' ', '')
        g = balance(r)
        print(r + ' - ' + g)
