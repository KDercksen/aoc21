#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

with open("input.txt") as f:
    bits = np.array(
        list(map(lambda x: [int(a) for a in x], map(str.strip, f.readlines()))),
    )
    print(bits.shape)


def bit_criteria(column):
    summed = np.sum(column)
    if column.shape[0] % 2 == 0:
        return summed >= (column.shape[0] // 2)
    else:
        return summed > (column.shape[0] // 2)


oxygen = bits[:]
co2 = bits[:]
for i in range(bits.shape[1]):
    print(i)
    if oxygen.shape[0] > 1:
        most_common = bit_criteria(oxygen[:, i])
        oxygen = oxygen[oxygen[:, i] == most_common, :]
        print(oxygen)
    if co2.shape[0] > 1:
        least_common = 1 - bit_criteria(co2[:, i])
        co2 = co2[co2[:, i] == least_common, :]
        print(co2)
    print("----")


powers = 2 ** np.arange(bits.shape[1])[::-1]
print(oxygen.dot(powers) * co2.dot(powers))
