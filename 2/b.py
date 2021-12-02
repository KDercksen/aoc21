#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    h, v, aim = 0, 0, 0
    for line in f:
        instruction, steps = line.split()
        if instruction == "forward":
            h += int(steps)
            v += int(steps) * aim
        elif instruction == "up":
            aim -= int(steps)
        else:
            aim += int(steps)
print(h * v)
