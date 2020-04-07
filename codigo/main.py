#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2019 João Paulo Paiva Lima <joao.lima1@estudante.ufla.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.pyplot as plt 
import numpy as np
from Perceptron import Perceptron
import random, math, os
from xlwt import Workbook 

def plotar(vum, vzero, tam, eta):
    
    v1=[]
    
    for i in range(tam):
        v1.append( abs(vum[i] - vzero[i]))
    plt.plot(range(tam), v1, label = ""+str(eta)+" eta") 
    
    
    plt.xlabel('jogada') 
     
    plt.ylabel('diferença') 
    
    plt.title('diferença entre a quantidade de zeros e uns em cada jogada') 
      
    plt.legend() 


class Jogador:
    
    def __init__(self, nome, rede = None):
        self.nome = nome
        self.rede = rede
        self.saida = 0
        self.vitorias = 0
        
    def jogar(self, inputs):
        if self.rede:
            self.saida = round(self.rede.ativar(inputs))
        return self.saida
    
    def treinar(self, correto, inputs):
        if self.rede:
            self.rede.treinar(correto - self.saida, inputs)

    def addVitorias(self, i, num = 1):
        self.vitorias += num
        
def main(args):
    
    numJogadores = 101
    numJogadas = 1000
    
    memoria = np.array( [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    jogadores = []
        
    for i in range(numJogadores):
        nome = "PerceptronSimples-" + str(i)
        p = Perceptron(numInputs = 13, taxaAprendizado = args)
        jogador = Jogador(nome, p)
        jogadores.append(jogador)


    #Essa parte e usada para escrever a planilha
    wb = Workbook() 
    sheet1 = wb.add_sheet('tabela') 
    for i in range(1, numJogadas+1):
        sheet1.write(i, 0, "jogada "+str(i)) 
    sheet1.write(0, 1, "Ums")
    sheet1.write(0, 2, "Zeros")
    #[fim] planilha

    vuns = []
    vzeros  = []

    for i in range(numJogadas):
        soma = 0
        jogadas = []
        
        for j in range(numJogadores):
            jogada = jogadores[j].jogar( memoria[-13:])
            jogadas.append( jogada)
            soma += jogada
            
        minoria = round(soma/numJogadores)*(-1) + 1
        
        for j in range(numJogadores):
            if jogadas[j] == minoria :
                jogadores[j].addVitorias(i)
            else:
                jogadores[j].treinar( minoria, memoria[-13:])
        
        vuns.append(soma)
        vzeros.append(numJogadores - soma)
        
        #Usado para planilha
        sheet1.write(i+1, 1, soma)
        sheet1.write(i+1, 2, numJogadores - soma)
        np.append(memoria, [minoria, ])
        #[fim] planilha
        
        os.system('clear')
        print(minoria)
        print(i)
    
    
    #salva a planilha
    wb.save('resultados/1000 - 101jogadores - 13inpts - '+str(args)+'eta.ods')
    
    #plota e salva o grafico
    plotar(vuns, vzeros,numJogadas, args)


for i in range (6):
    main(round(1/math.pow((i*4 + 0.8), 2), 3))
    plt.savefig('../gráfico - Zeros e Uns - variaçao de eta- 01.png') 
