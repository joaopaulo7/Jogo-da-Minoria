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
import tensorflow as tf
import numpy as np
from Perceptron import Perceptron
import random, math, os
from xlwt import Workbook 

class Jogador:
    
    def __init__(self, nome, rede = None, tipoRede = "simples"):
        self.nome = nome
        self.rede = rede
        self.saida = 0
        self.vitorias = 0
        self.tipoRede = tipoRede
        
    def jogar(self, inputs):
        if self.rede:
            if self.tipoRede == 'simples':
                self.saida = round(self.rede.ativar(inputs))
            else:
                self.saida = round(float(self.rede.predict(np.array([inputs, ]))[0][0]))
        else:
            self.saida =  random.randint(0, 1)
        return self.saida
    
    def treinar(self, correto, inputs):
        if self.rede and self.tipoRede == 'simples' :
            self.rede.treinar(correto - self.saida, inputs)
        elif self.rede:
            self.rede.fit( x = np.array([inputs, ]), y = np.array([correto, ]), batch_size = 1, epochs=1,  verbose = 0)

    def addVitorias(self, i, num = 1):
        self.vitorias += num
        
memoria = np.array( [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
jogadores = []

for i in range(0):
    nome = "Aleatorio-" + str(i)
    jogador = Jogador(nome)
    jogadores.append(jogador)
    
for i in range(100):
    nome = "PerceptronSimples-" + str(i)
    p = Perceptron(numInputs = 11, taxaAprendizado = .001)
    jogador = Jogador(nome, p)
    jogadores.append(jogador)
    
k= tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='relu', input_shape=(11,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

k.compile(optimizer='Adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

jogadores.append( Jogador("RedeDupla-0", k, "complexa"))

r= 1000

wb = Workbook() 
sheet1 = wb.add_sheet('1x10e+3-001') 
for i in range(101):
    sheet1.write(0, i, jogadores[i].nome) 

for i in range(r):
    soma = 0
    jogadas = []
    
    for j in range(101):
        jogada = jogadores[j].jogar(memoria[-11:])
        jogadas.append( jogada)
        soma += jogada
        
    minoria = round(soma/101)*(-1) + 1
    
    for j in range(101):
        if jogadas[j] == minoria :
            jogadores[j].addVitorias(i)
        jogadores[j].treinar( minoria, memoria[-11:])
        
        sheet1.write(i+1, j, jogadores[j].vitorias)
    np.append(memoria, [minoria, ])
    
    os.system('clear')
    print(i)


for i in range(101):
    print( jogadores[i].nome + "->" + str(jogadores[i].vitorias) + " Vitorias")

wb.save('teste1000-num.xls')
