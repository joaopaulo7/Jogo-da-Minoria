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
from Perceptron import Perceptron
import random, math
        
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
                self.saida = round(float(self.rede.predict((inputs,))[0]))
        else:
            self.saida =  random.randint(0, 1)
        return self.saida
    
    def treinar(self, correto, inputs):
        if self.rede and self.tipoRede == 'simples' :
            self.rede.treinar(correto - self.saida, inputs)
        elif self.rede:
            self.rede.fit( x = (inputs, ), y = ((correto,), ), batch_size = 1, epochs=1)

    def addVitorias(self, num = 1):
        self.vitorias += num
        
memoria = 0, 0, 0
jogadores = []

for i in range(50):
    nome = "Aleatorio-" + str(i)
    jogador = Jogador(nome)
    jogadores.append(jogador)
    
for i in range(50):
    nome = "PerceptronSimples-" + str(i)
    p = Perceptron(numInputs = 3, taxaAprendizado = 0.1)
    jogador = Jogador(nome, p)
    jogadores.append(jogador)
    
k= tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

k.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

jogadores.append( Jogador("RedeDupla-0", k, "complexa"))

for i in range(100):
    soma = 0
    jogadas = []
    
    for j in range(101):
        jogada = jogadores[j].jogar(memoria[-3:])
        jogadas.append( jogada)
        soma += jogada
        
    minoria = (round(soma/100)*(-1) + 1)*0.999999
    
    for j in range(101):
        if jogadas[j] == round(minoria) :
            jogadores[j].addVitorias()
        else:
            jogadores[j].treinar(minoria, memoria[-3:])
            
    memoria + (minoria,)
    
    
    print("A MINORIA FOI:" + str(minoria))
    for i in range(101):
        print( jogadores[i].nome + "->" + str(jogadas[i]))

for i in range(101):
    print( jogadores[i].nome + "->" + str(jogadores[i].vitorias) + " Vitorias")

