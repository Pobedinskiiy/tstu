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

        return tokens
