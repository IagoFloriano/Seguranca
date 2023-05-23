#!/usr/bin/env python3
import crypt as c
import sys as s
import os

# senhas:
# $y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5
# $y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00

def main():
    if len(s.argv) != 3:
        print("Uso: " + s.argv[0] + " <senha> <dicionario onde a senha sera procurada")
        print("OBS: senha deve estar no formato gerado pelo yescript e com o salt")
    dicionario = open(s.argv[2], 'r')
    senha = s.argv[1]
    salt = (s.argv[1])[:29]

    for palavra in dicionario:
        palavra = palavra.strip()
        tentativa = c.crypt(palavra, salt)
        if tentativa == senha:
            print("senha descoberta foi: " + palavra)
            print("com yescript: " + tentativa)
            break


if __name__ == '__main__':
    main()
