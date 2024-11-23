class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
            print(self.current_token)
        else:
            self.current_token = None

    def parse(self):
        print("Начинаем парсинг программы.")
        self.program()
        print("Парсинг завершён.")

    def program(self):
        self.statements()

    def statements(self):
        print("Анализируем оператор(ы) в программе.")
        self.statement()
        while self.current_token == ';':
            self.next_token()
            self.statement()

    def statement(self):
        print(f"Текущий токен: {self.current_token}")
        if self.current_token == 'if':
            self.conditional_statement()
        elif self.current_token == 'writeln':
            self.output_statement()
        elif self.current_token.isidentifier():
            self.assignment()
        else:
            self.error()

    def conditional_statement(self):
        print("Анализ условия (if).")
        self.match('if')
        self.conditional_expression()
        self.match('THEN')
        self.statements()
        if self.current_token == 'else':
            self.match('else')
            self.statements()

    def conditional_expression(self):
        print("Анализ условного выражения.")
        self.arithmetic_expression()
        if self.current_token in ['<>', '=', '<=', '>=', '<', '>']:
            self.match(self.current_token)
            self.arithmetic_expression()
        else:
            self.error()

    def assignment(self):
        print("Анализ присваивания.")
        id = self.current_token
        self.match(id)
        self.match(':=')
        self.arithmetic_expression()

    def arithmetic_expression(self):
        print("Анализ арифметического выражения.")
        self.term()
        while self.current_token in ['+', '-']:
            self.match(self.current_token)
            self.term()

    def term(self):
        print("Анализ слогаемого")
        self.factor()
        while self.current_token in ['*', '/']:
            self.match(self.current_token)
            self.factor()

    def factor(self):
        print("Анализ множителя")
        if self.current_token.isidentifier():
            self.match(self.current_token)
        elif self.current_token.isdigit():
            self.match(self.current_token)
        else:
            self.error()

    def output_statement(self):
        print("Анализ оператора вывода.")
        self.match('writeln')
        self.match('(')
        if self.current_token.isidentifier() or self.current_token.isdigit():
            self.match(self.current_token)
        self.match(')')

    def match(self, expected_token):
        if self.current_token == expected_token:
            print(f"Сопоставлен: {expected_token}")
            self.next_token()
        else:
            self.error()

    def error(self):
        raise Exception(f"Синтаксическая ошибка: неожиданный токен: {self.current_token}")

def tokenize(code):
    tokens = []
    code = code.replace('(', ' ( ').replace(')', ' ) ')
    code = code.replace(',', ' , ')
    for token in code.split():
        if token.isidentifier() or token.isdigit() or token in ['if', 'THEN', 'else', 'writeln', ':=', '+', '-', '*', '/', '<', '>', '<=', '>=', '=', '<>']:
            tokens.append(token)
    return tokens

code = """
if (X + Y) <> 0 THEN
A := (X * X + Z * Z) / (1 + 1 / (X - Y * Z))
else A := 0;
writeln(A)
"""

tokens = tokenize(code)
print(tokens)
parser = Parser(tokens)
try:
    parser.parse()
    print("Код успешно разобран.")
except Exception as e:
    print(f"Ошибка разбора: {e}")