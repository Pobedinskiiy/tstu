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
        self.ident_ptr = []
        self.hash_ident = {}

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
                self.add_ident(token, "float")

        return tokens

    def add_ident(self, ident: str, type_ident: str) -> None:
        h = self.hash_func(ident)
        logging.debug(f"Ид: {ident} - хеш: {h}")

        if h not in self.hash_ident:
            self.hash_ident[h] = len(self.ident_ptr)
        else:
            index = self.ident_ptr[self.hash_ident[h]][2]
            if index == 0:
                self.ident_ptr[self.hash_ident[h]][2] = len(self.ident_ptr)
            else:
                while self.ident_ptr[index][2] != 0:
                    index = self.ident_ptr[index][2]
                self.ident_ptr[index][2] = len(self.ident_ptr)
        self.ident_ptr.append([ident, type_ident, 0])

        logging.debug(f"Хеш таблица: {self.hash_ident}, таблица ссылок индентификаторов: {self.ident_ptr}")

    def show_chain(self):
        logging.info("Хеш таблица:")
        logging.info(self.hash_ident)
        for i in range(len(self.ident_ptr)):
            logging.info(self.ident_ptr[i])

    @staticmethod
    def hash_func(ident: str) -> int:
        return sum([ord(i) for i in ident])