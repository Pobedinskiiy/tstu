import re


class Decoder:
    lexemes: dict = {
        "if": " 1 ",
        "THEN": " 2 ",
        "else": " 3 ",
        "writeln": " 4 ",
        "(": " 5 ",
        ")": " 6 ",
        ":=": " 7 ",
        "-": " 8 ",
        "+": " 9 ",
        "/": " 10 ",
        "*": " 11 ",
        "<>": " 14 ",
        "<": " 12 ",
        ">": " 13 ",
        ";": " 15 ",
        "number": " 16"
    }

    def __init__(self) -> None:
        self.code: str = ""

    def decoding(self, code: str) -> str:
        self.code = code
        for number in set(re.findall(r'\d+', code)):
            self.code = self.code.replace(number, f"number[{number}]")
        for key, value in self.lexemes.items():
            self.code = self.code.replace(key, value)
        for variable in list(set(self.code.split())):
            if len(set(re.findall(r'\d+', variable))) == 0:
                self.code = self.code.replace(variable, f"17[{variable}]")
        self.code = re.sub(" +", " ", self.code)
        self.code = self.code.replace("\n ", "\n")
        if self.code[0] == " ":
            return self.code[1:]
        return self.code