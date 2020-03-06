#!/usr/bin/env python3
import CPU_Temp as cpu
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1, 20, 90])

i = 0

while(True):
    i += 1
    y = cpu.cpu_temp()
    plt.axis([0, i, 20, y+20])
    plt.scatter(i, y, c="blue",)
    plt.pause(0.05)

plt.show()
