#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

def plot():
    data1 = pd.read_csv("1c.csv")
    data2 = pd.read_csv("1crs.csv")
    data3 = pd.read_csv("1ers.csv")
    data4 = pd.read_csv("2c.csv")
    data5 = pd.read_csv("2crs.csv")

    plt.figure()
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')

    plt.plot(data3['effort'], data3.iloc[:, 2:].mean(axis=1), color='blue', label='1-Evol-RS', marker ='o', markevery = 25, markeredgecolor='black', linewidth = 0.5)
    plt.plot(data2['effort'], data2.iloc[:, 2:].mean(axis=1), color='green', label='1-Coev-RS', marker ='v', markevery = 25, markeredgecolor='black', linewidth = 0.5)
    plt.plot(data5['effort'], data5.iloc[:, 2:].mean(axis=1), color='red', label='2-Coev-RS', marker ='h', markevery = 25, markeredgecolor='black', linewidth = 0.5)
    plt.plot(data1['effort'], data1.iloc[:, 2:].mean(axis=1), color='black', label='1-Coev', marker ='s', markevery = 25, markeredgecolor='black', linewidth = 0.5)
    plt.plot(data4['effort'], data4.iloc[:, 2:].mean(axis=1), color='magenta', label='2-Coev', marker ='D', markevery = 25, markeredgecolor='black', linewidth = 0.5)

    plt.legend()
    plt.axis([0, 500000, 0.60, 1.00])

    plt.show()


if __name__ == '__main__':
    plot()