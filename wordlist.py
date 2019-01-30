#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

words = []

print()
name = str(input(" Victim's first name > "))
print()
words.append(name)
words.append(name.lower())
words.append(name.upper())
surname = str(input(" Victim's surname > "))
print()
words.append(surname)
words.append(surname.lower())
words.append(surname.upper())
words.append(name + surname)
words.append(name + "_" + surname)
words.append(name.upper() + surname)
words.append(name.lower() + surname)
words.append(name + surname.upper())
words.append(name + surname.lower())
words.append(name.upper() + surname.upper())
words.append(name.lower() + surname.lower())
nickname = str(input(" Victim's nickname > "))
if nickname != "":
    words.append(nickname)
    words.append(nickname.lower())
    words.append(nickname.upper())

for i in range(1, 3):
    n = 3
    s = 2
    nick = 1

    if n > s and n > nick:
        newword = name + surname + nickname
        words.append(newword)
        words.append(newword.lower())
        words.append(newword.upper())
        newword = name.upper() + surname + nickname
        words.append(newword)
        newword = name.lower() + surname + nickname
        words.append(newword)
        newword = name + surname.upper() + nickname
        words.append(newword)
        newword = name + surname.lower() + nickname
        words.append(newword)
        newword = name + surname.upper() + nickname
        words.append(newword)
        newword = name + surname.lower() + nickname
        words.append(newword)
        newword = name + surname + nickname.upper()
        words.append(newword)
        newword = name + surname + nickname.lower()
        words.append(newword)

        newword2 = name + nickname + surname
        words.append(newword2)
        words.append(newword2.lower())
        words.append(newword2.upper())
        newword2 = name.upper() + nickname + surname
        words.append(newword2)
        newword2 = name.lower() + nickname + surname
        words.append(newword2)
        newword2 = name + nickname.upper() + surname
        words.append(newword2)
        newword2 = name + nickname.lower() + surname
        words.append(newword2)
        newword2 = name + nickname + surname.upper()
        words.append(newword2)
        newword2 = name + nickname + surname.lower()
        words.append(newword2)

        n = 1

        if s > nick:
            s = 2
            nick = 3
        else:
            s = 3
            nick = 2


print()
print()
print()
numerosfrente = str(input(" Do you want passwords ended up by numbers [Y/N] > "))
if numerosfrente == 'Y' or numerosfrente == 'y':
    algarismos = int(input(" Numeros de quantos algarismos? > "))
    al = 0
    while len(str(al)) <= algarismos:
        plvralgarismo = name + str(al)
        words.append(plvralgarismo)
        plvralgarismo = name + surname + str(al)
        words.append(plvralgarismo)
        words.append(plvralgarismo.upper())
        words.append(plvralgarismo.lower())
        plvralgarismo = name.upper() + surname + str(al)
        words.append(plvralgarismo)
        plvralgarismo = name.lower() + surname + str(al)
        words.append(plvralgarismo)
        plvralgarismo = name + surname.upper() + str(al)
        words.append(plvralgarismo)
        plvralgarismo = name + surname.lower() + str(al)
        words.append(plvralgarismo)
        al = al + 1

    alu = 0
    while len(str(alu)) <= algarismos:
        plvralgarismou = name + "_" + str(alu)
        words.append(plvralgarismo)
        plvralgarismou = name + surname + "_" + str(alu)
        words.append(plvralgarismou)
        words.append(plvralgarismou.upper())
        words.append(plvralgarismou.lower())
        plvralgarismou = name.upper() + surname + "_" + str(al)
        words.append(plvralgarismou)
        plvralgarismou = name.lower() + surname + "_" + str(al)
        words.append(plvralgarismou)
        plvralgarismou = name + surname.upper() + "_" + str(al)
        words.append(plvralgarismou)
        plvralgarismou = name + surname.lower() + "_" + str(al)
        words.append(plvralgarismou)
        alu = alu + 1

    for i in range (1, 10):
        words.append(name + "0" + str(i))
        words.append(name.upper() + "0" + str(i))
        words.append(name.lower() + "0" + str(i))
        words.append(name + surname + "0" + str(i))
        words.append(name.upper() + surname + "0" + str(i))
        words.append(name.lower() + surname + "0" + str(i))
        words.append(name + surname.upper() + "0" + str(i))
        words.append(name + surname.lower() + "0" + str(i))
        words.append(name + surname + "_" + "0" + str(i))
        words.append(name + surname + "_" + "0" + str(i))
        words.append(name + "_" + surname + "_" "0" + str(i))
            
print()
bdate = str(input(" Victim's birthday date(DD/MM/yYYY) > "))
print()
favnumber = str(input(" Victim's favourite number > "))
print()
print()
print()

f = open(name+".lst","w+")
for palavra in words:
    f.write(palavra+"\n")
f.close()

print("Geradas " + str(len(words)) + " palavras para o arquivo "+name+".lst.")
print("Boa Sorte!")
