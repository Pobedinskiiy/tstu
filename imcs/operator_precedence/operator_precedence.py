import logging


class OperatorPrecedence:
    def __init__(self) -> None:
        self.matrix = None
        self.tokens, self.lexemes = None, None

    def parse_syntactically(self, tokens: list, lexemes: dict) -> None:
        self.tokens, self.lexemes = tokens, lexemes
        self.open_md()
        self.disassemble()

    def open_md(self) -> None:
        with open("operator_precedence/README.md", 'r', encoding='utf8') as file:
            self.matrix = {}
            header = []
            for line in file.readlines():
                if line[0] == '|' and line[1] != ':':
                    line = line.strip()
                    row = line.strip('|').split('|')
                    for i in range(len(row)):
                        row[i] = row[i].strip().strip('`')

                    if len(header) == 0:
                        header = row[1:]
                        for i in range(len(header)):
                            header[i] = self.lexemes[header[i]]
                    else:
                        lexeme = row[0]
                        matrix_row = {}
                        for i, l in enumerate(row[1:]):
                            if l != "":
                                matrix_row[header[i]] = l
                        self.matrix[self.lexemes[lexeme]] = matrix_row

        logging.debug(self.matrix)

    def _get_lexeme(self, i: int) -> int:
        if type(self.tokens[i]) is list:
            return self.tokens[i][0]
        return self.tokens[i]

    def disassemble(self):
        k = len(self.tokens)
        n1, n2 = 0, 0
        while True:
            i = 1
            s = "<"
            while i < k:
                n1 = self._get_lexeme(i - 1)
                n2 = self._get_lexeme(i)
                s += str(n1) + str(self.matrix[n1][n2])
                if self.matrix[n1][n2] == ">":
                    break
                i += 1

            s += str(n2) + ">"
            logging.debug(f"Цепочка операторного предшествия: {s}")
            j2 = i - 1
            j1 = j2
            while True:
                j1 = j1 - 1
                n1 = self._get_lexeme(j1)
                n2 = self._get_lexeme(j1 + 1)
                if j1 < 0 or self.matrix[n1][n2] == "<":
                    break
            for x in range(j1 + 1, i):
                logging.debug(f"Текущий токен: {self.tokens[x]}")

            j = j1
            for x in range(i, k):
                j += 1
                self.tokens[j] = self.tokens[x]
                self.tokens[j + 1] = 0
            k -= j2 - j1

            if k <= 1:
                logging.debug(f"Текущий токен: {self._get_lexeme(0)}")
                break