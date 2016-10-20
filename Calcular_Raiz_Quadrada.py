#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/19/2016 U.S.A


import math

### Programa para saber raiz quadrada!

raiz_resposta = float(input('Digite o numero (x): '))
print(type(raiz_resposta))
resposta = float(math.sqrt(raiz_resposta))
print(type(resposta))
print('Valor inserido: ' + str(raiz_resposta))
print('Valor da Raiz: ' + str(resposta))
