#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

for i in range(10, 100):
    x = i//10+i%10
    if i == x+x*x:
        print(i)
