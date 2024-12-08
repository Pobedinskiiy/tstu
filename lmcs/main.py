from copy import copy

from log import init_logging, logging
from decoder import Decoder
from recursive_descent import RecursiveDescent
from operator_precedence import OperatorPrecedence


init_logging()

code = """
if (X+Y)<>0 THEN
A:=(X*X+Z*Z)/(1+1/(X-Y*Z))
else A:=0;
writeln (A)
"""

logging.info(f"Код программы: {code}")

decoder = Decoder()
tokens = decoder.decoding(code)

logging.info(f"Декодированная программа: {tokens}")

recursive_descent = RecursiveDescent()
try:
    recursive_descent.parse_syntactically(copy(tokens))
    logging.info("Метод рекурсивного спуска не выявил ошибок в коде")
except Exception as e:
    logging.critical(f"Ошибка разбора: {e}")

operator_precedence = OperatorPrecedence()
try:
    operator_precedence.parse_syntactically(copy(tokens), copy(decoder.lexemes))
    logging.info("Метод операторного предшествия не выявил ошибок в коде")
except Exception as e:
    logging.critical(f"Ошибка разбора: {e}")
