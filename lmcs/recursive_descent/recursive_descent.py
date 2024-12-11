import logging


class RecursiveDescent:
    def __init__(self) -> None:
        self.tokens = None
        self.current_token = None

    def parse_syntactically(self, tokens: list) -> None:
        self.tokens = tokens
        self.current_token = None
        logging.debug("Начинаем парсинг программы.")
        self.statements()
        logging.debug("Парсинг завершён.")

    def statements(self):
        logging.debug("Анализируем оператор(ы) в программе.")
        self.next_token()
        self.statement()
        while self.current_token == 13:
            logging.debug("Следующий сегмент")
            self.next_token()
            self.statement()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
            logging.debug(f"Текущий токен: {self.current_token}")
        else:
            self.current_token = None

    def statement(self):
        if self.current_token == 1:
            self.conditional_statement()
        elif self.current_token == 4:
            self.output_statement()
        elif self.current_token[0] == 15:
            self.assignment()
        else:
            self.error()

    def conditional_statement(self):
        logging.debug("Анализ условия (if).")
        self.match(1)
        self.conditional_expression()
        self.match(2)
        self.statement()
        if self.current_token == 3:
            self.match(3)
            self.statement()

    def conditional_expression(self):
        logging.debug("Анализ условного выражения.")
        self.arithmetic_expression()
        if self.current_token in [12]:
            self.match(self.current_token)
            self.arithmetic_expression()
        else:
            self.error()

    def assignment(self):
        logging.debug("Анализ присваивания.")
        self.match(self.current_token)
        self.match(7)
        self.arithmetic_expression()

    def arithmetic_expression(self) -> None:
        logging.debug("Анализ арифметического выражения.")
        self.term()
        while self.current_token in [8, 9]:
            self.match(self.current_token)
            self.term()

    def term(self) -> None:
        logging.debug("Анализ слагаемого")
        self.factor()
        while self.current_token in [10, 11]:
            self.match(self.current_token)
            self.factor()

    def factor(self) -> None:
        logging.debug("Анализ множителя")
        if self.current_token == 5:
            self.match(5)
            self.arithmetic_expression()
            self.match(6)
        elif self.current_token[0] in [14, 15]:
            self.match(self.current_token)
        else:
            self.error()

    def output_statement(self) -> None:
        logging.debug("Анализ оператора вывода.")
        self.match(4)
        self.match(5)
        if self.current_token[0] in [14, 15]:
            self.match(self.current_token)
        self.match(6)

    def match(self, expected_token) -> None:
        if self.current_token == expected_token:
            logging.debug(f"Сопоставлен: {expected_token}")
            self.next_token()
        else:
            self.error()

    def error(self) -> None:
        raise Exception(f"Синтаксическая ошибка: неожиданный токен: {self.current_token}")
