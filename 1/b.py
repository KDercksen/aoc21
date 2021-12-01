#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    measurements = list(map(int, f.readlines()))

print(
    sum(
        sum(measurements[i : i + 3]) > sum(measurements[i - 1 : i + 2])
        for i in range(1, len(measurements) - 2)
    )
)
