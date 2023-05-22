---
title: Trabalho 3
subtitle: Segurança
author: Iago Mello Floriano 
date: GRR20196049
---

# Ideia geral

A ideia geral desse relatório é informar como foi feito a quebra de três senhas dado
suas versões criptografadas, a primeira senha criptografada com md5 e as outras duas
senhas criptografadas com yescript.

Para as três senhas foi usado um dicionario para se tentar achar a senha, os dicionários
usados foram:

- dicionario.txt ('/usr/share/dict/brazilian' nas máquinas do dinf) um dicionário em portugues
- rockyou.txt ([https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)) um banco de senhas comuns

# Senha 1

Como mencionado anteriormente, esse senha foi criptografada com md5. A senha é a seguinte:
e8d95a51f3af4a3b134bf6bb680a213a

Para essa quebra foi usada o seguinte script em python

`md5.py:`
```python
#!/usr/bin/env python3
import hashlib as h

def main():
    dictfile = open('dicionario.txt')
    dictlines = dictfile.readlines()

    for line in dictlines:
        word = line.strip()
        md5 = h.md5(word.encode()).hexdigest()
        if md5 == 'e8d95a51f3af4a3b134bf6bb680a213a':
            print("senha descoberta foi " + word)
            print("com md5 " + md5)
            break


if __name__ == '__main__':
    main()
```

Rodando `time md5.py` temos a seguinte saída:

```
senha descoberta foi senha
com md5 e8d95a51f3af4a3b134bf6bb680a213a
./md5.py  0,17s user 0,01s system 99% cpu 0,175 total
```

Com isso sabemos que a senha era `senha` e demorou apenas demorou `0,17 segundos`.

# Senha 2 e 3

As senhas 2 e 3 foram criptografadas com yescript, sabemos isso pelo formato delas.
Senhas que são da forma `$y${salt}$____` são criptografadas com yescript. As senhas são
as seguintes:

1. `$y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00`
2. `$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5`

`yescript.py`
```python
#!/usr/bin/env python2
import crypt as c
import sys as s
import os

def main():
    if len(s.argv) != 3:
        print("Uso: " + s.argv[0] + " <senha> <dicionario onde a senha sera procurada>")
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
```

Rodando `time yescript.py` para a senha 1 com o dicionario.txt temos:
```
senha descoberta foi: abacate
com yescript: $y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00
./yescript.py  dicionario.txt  40,22s user 6,60s system 99% cpu 47,053 total
```
Apenas 40 segundos para conseguir uma senha, não está nada mal.

Houve uma tentativa de roda o `yescript.py` para a senha 2 com o dicionario.txt, porém
a senha não foi encontrada, então, foi usado o rockyou.txt como banco de palavras. Obtive
, então, os seguintes resultados:
