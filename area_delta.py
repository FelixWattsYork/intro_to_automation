import miller
import numpy as np
import matplotlib.pyplot as plt
import os

def area(r, z):
    # abs because (r, z) start on the out-board midplace and r decreases
    return np.abs(np.trapezoid(z, r))


def area_vs_delta(area, delta, savefig):
    """
    Help on funciton plot_surface in module mille.py

    plots a flux surface in 2d
    """
    plt.plot(area, delta)
    plt.xlabel("area")
    plt.ylabel("delta")
    if savefig:
        plt.savefig(os.getcwd() + "/felix.png")

def main():
    A = 2.2
    kappa = 1.5
    R0 = 2.5
    deltas = np.linspace(0.1, 0.5,num = 50)
    areas = []
    for _,delta in enumerate(deltas):
        R_s, Z_s = miller.flux_surface(A, kappa, delta, R0)
        areas.append(area(R_s,Z_s))
    area_vs_delta(areas, deltas, True)
if __name__ == "__main__":
    main()