# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:32:25 2026

@author: BabakMehr
"""

my_set_1 = {"arefeh" ,"ali" ,"sara"}
print(my_set_1)
my_set_2 = {"atena" ,"ali" ,"hassan"}
print(my_set_2)
print(my_set_1.difference(my_set_2))
print(my_set_2.union(my_set_1))
print(my_set_1.intersection(my_set_2))

my_set_1.add("zahra")
print(my_set_1)
my_set_2.update(["arash" ,"hossein"])
print(my_set_2)

my_set_2.pop()
print(my_set_2)
my_set_1.clear()
print(my_set_1)

