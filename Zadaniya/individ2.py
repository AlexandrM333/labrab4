#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a1 = float(input("Введите a1 "))
a2 = float(input("Введите a2 "))
b1 = float(input("Введите b1 "))
b2 = float(input("Введите b2 "))
c1 = float(input("Введите c1 "))
c2 = float(input("Введите c2 "))

  if a1/a2 == b1/b2 and a1/a2 == c1/c2:
    print("Прямые наложены друг на друга")
  elif a1 == a2 or a1*b2-a2*b1 == 0:
    print("Прямые параллельны")
  else:
    x = (b2*c1+b1*c1)/(b2*a1-b1*a2)
    y = (-c2-a2*x)/b2
    print("Координаты точек пересечения (",y,":",x,")")
