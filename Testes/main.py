#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 João Paulo Paiva Lima <joao.lima1@estudante.ufla.br>
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

import random, math
from Perceptron import Perceptron

def getAnimal(mamal = False):
    animal = []
    if(mamal):
        animal.append((random.randint(0,100000)+1)/100000)
        animal.append(2/8)
        animal.append((random.randint(0,7)+3)/10)
        animal.append(True)
        animal.append(True)
    else:
        animal.append((random.randint(0,10000)+1)/500000)
        animal.append(random.randint(0,8)/8)
        animal.append(random.randint(0,9)/10)
        animal.append(bool(random.randint(0,1)))
        animal.append(bool(random.randint(0,1)))
    return animal
        


p = Perceptron(5, 0.3)
animal = []
i = 0
while(i < 100):
    mamal = (random.randint(0,1))
    animal = [mamal, getAnimal(mamal)]
    saida = p.ativar(animal[1])
    print(saida)
    if( not((saida > 0.5) == mamal)):
        print(animal)
        print("[ERRO]")
        p.treinar((saida - int(mamal)), animal[1])
        i =0
    else:
        i = i+1
        print(animal)
        print("[ACERTO]")
