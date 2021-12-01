#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    measurements = list(map(int, f.readlines()))

print(sum(a > b for a, b in zip(measurements[1:], measurements)))
