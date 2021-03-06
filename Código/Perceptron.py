#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Perceptron.py
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
import random, math, numpy as np

def sigmoid(x):
    if(x < -10):
        return 1
    elif(x > 10):
        return 0
    else:
        return 1 / (1 + math.exp(-x))
        
def tanhOp(x):
    if(x < -10):
        return 1
    elif(x > 10):
        return 0
    else:
        return math.tanh(x)
        
        
class Perceptron:
    
    def __init__(self, numInputs, taxaAprendizado, bias = None, semente = None):
    
        self.numInputs = numInputs
        self.taxa = taxaAprendizado
        self.pesos = []
        
        if(semente):
            random.seed(semente)
        
        if bias:
            self.bias = bias
        else:
            self.bias = round(random.random()*2-1, 3)
            print(self.bias)
        
        
        for i in range(numInputs):
            self.pesos.append(round(random.random()*2-1, 3))
        
    def ativar(self, inputs):
        
        soma = 0.0
        for i in range(self.numInputs):
            soma += inputs[i]*self.pesos[i]
        x =  (soma + self.bias)
        if(x == 0):
            return 1
        return  np.sign(x)
        
    def treinar(self, erro, inputs):
            
        for i in range(self.numInputs):
            self.pesos[i]  =  self.pesos[i] + (self.taxa*erro*inputs[i])
            
        self.bias = self.bias + self.taxa*erro
