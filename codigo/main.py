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
    
    def __init__(self, nome, rede = None):
        self.nome = nome
        self.rede = rede
        self.saida = 0
        self.vitorias = 0
        
        
    def jogar(self, inputs):
        if self.rede:
            self.saida = round(self.rede.ativar(inputs))
        else:
            self.saida =  random.randint(0, 1)
        return self.saida
    
    def treinar(self, correto, inputs):
        if self.rede :
            self.rede.treinar(correto - self.saida, inputs)

    def addVitorias(self, num = 1):
        self.vitorias += num
        
memoria = 0, 0, 0
tamMemoria = 3
jogadores = []

for i in range(50):
    nome = "Aleatorio-" + str(i)
    jogador = Jogador(nome)
    jogadores.append(jogador)
    
for i in range(50):
    nome = "PerceptronSimples-" + str(i)
    p = Perceptron(numInputs = 3, taxaAprendizado = 0.01)
    jogador = Jogador(nome, p)
    jogadores.append(jogador)

for i in range(1000):
    soma = 0
    jogadas = []
    
    for j in range(100):
        jogada = jogadores[j].jogar(memoria[:3])
        jogadas.append( jogada)
        soma += jogada
        
    minoria = round(soma/100)*(-1) + 1
    
    for j in range(100):
        if jogadas[j] == minoria :
            jogadores[j].addVitorias()
        else:
            jogadores[j].treinar(minoria, memoria[-3:])
            
    for i in range(100):
        print( jogadores[i].nome + "->" + str(jogadas[i]))

for i in range(100):
    print( jogadores[i].nome + "->" + str(jogadores[i].vitorias) + " Vitorias")

