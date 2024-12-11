import logging


class Decoder:
    lexemes: dict = {
        "if": 1,
        "THEN": 2,
        "else": 3,
        "writeln": 4,
        "(": 5,
        ")": 6,
        ":=": 7,
        "-": 8,
        "+": 9,
        "/": 10,
        "*": 11,
        "<>": 12,
        ";": 13,
        "const": 14,
        "id": 15
    }

    def __init__(self):
        self.ident_map = {}
        self.ident_matrix_cursor = -1
        self.ident_matrix = []
        self.hash_matrix = {}

    def decoding(self, code: str) -> list:
        logging.debug(f"Лексемы словаря: {self.lexemes}")

        tokens = []
        for key in self.lexemes.keys():
            code = code.replace(key, f" {key} ")

        for token in code.split():
            val = self.lexemes.get(token)
            if val is not None:
                tokens.append(self.lexemes.get(token))
            elif token.isdigit():
                tokens.append([14, token])
            elif token.isidentifier():
                tokens.append([15, token])
                self.add_ident(token)

        return tokens

    def add_ident(self, ident: str) -> None:
        h = self.hash_func(ident)
        logging.debug(f"Ид: {ident} - хеш: {h}")
        self.ident_matrix_cursor += 1
        self.ident_matrix.append([ident, 0, 0])

        if h not in self.hash_matrix:
            self.hash_matrix[h] = self.ident_matrix_cursor
        else:
            ident = self.hash_matrix[h]
            while self.ident_matrix[ident][2] != 0:
                ident = self.ident_matrix[ident][2]
            self.ident_matrix[ident][2] = self.ident_matrix_cursor

        if ident not in self.ident_map:
            self.ident_map[ident] = len(self.ident_map)

        logging.debug(f"Хеш таблица: {self.hash_matrix} {self.ident_matrix}")

    def show_chain(self):
        logging.info("Хеш таблица:")
        logging.info(self.hash_matrix)
        logging.info(self.ident_matrix)

    @staticmethod
    def hash_func(ident: str) -> int:
        return sum([ord(i) for i in ident])