#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    h, v = 0, 0
    for line in f:
        instruction, steps = line.split()
        if instruction == "forward":
            h += int(steps)
        elif instruction == "up":
            v -= int(steps)
        else:
            v += int(steps)
print(h * v)
