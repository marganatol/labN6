# -*- coding: utf-8 -*-
num = int(input('Введите число, включающее только цифры 6 и/или 9: '))
def rot(num):
    return int(str(num).replace("6","9", 1))
print(rot(num))