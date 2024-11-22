from decoder import Decoder

with open("temp/code.txt", "r") as file:
    code = file.read()

print("/*--------------------------*/")
print(code)
decoder = Decoder()
decode = decoder.decoding(code)
print("/*--------------------------*/")
print(decode)

with open("temp/decode.txt", "w") as file:
    file.write(decode)
