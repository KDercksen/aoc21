#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

with open("input.txt") as f:
    bits = np.array(
        list(map(lambda x: [int(a) for a in x], map(str.strip, f.readlines())))
    )

most_common = np.sum(bits, axis=0) > (bits.shape[1] // 2)
least_common = ~most_common
powers = 2 ** np.arange(most_common.size)[::-1]

print(most_common.dot(powers) * least_common.dot(powers))
