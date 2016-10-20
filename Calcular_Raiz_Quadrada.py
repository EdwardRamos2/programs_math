#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/19/2016 U.S.A


import math                 #Importa o modulo (math) Matematica

### Programa para saber raiz quadrada!

raiz_resposta = float(input('Digite o numero (x): '))   #Valor a ser inserido pelo usuario! Convertendo em ponto flutuante a entrada
print(type(raiz_resposta))                              #Saida usando a funcao type para saber o tipo da variavel inserida.
resposta = float(math.sqrt(raiz_resposta))              #Calculo usando o modulo math, com a funcao sqrt para calculo de Raiz.
print(type(resposta))                                   #Saida usando novamente a funcao type, para saber o tipo.
print('Valor inserido: ' + str(raiz_resposta))          #Saida valor inserido pelo usuario.
print('Valor da Raiz: ' + str(resposta))                #Saida calculado a raiz quadrada da entrada do usuario.
