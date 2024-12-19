from numpy import pi, cos, sin, arcsin, linspace
import matplotlib.pyplot as plt
import os


def plot_surface(R_s, Z_s, savefig):
    """
    Help on funciton plot_surface in module mille.py

    plots a flux surface in 2d
    """
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig:
        plt.savefig(os.getcwd() + "/miller.png")


def flux_surface(A, kappa, delta, R0):
    """
    Help on funciton flux_surface in module mille.py

    calculates a flux surface for a given A,kappa, delta, R0
    """
    theta = linspace(0, 2 * pi)
    r = R0 / A
    R_s = R0 + r * cos(theta + (arcsin(delta) * sin(theta)))
    Z_s = kappa * r * sin(theta)
    return R_s, Z_s


def main():
    A = 2.2
    kappa = 1.5
    delta = 0.3
    R0 = 2.5
    R_s, Z_s = flux_surface(A, kappa, delta, R0)
    plot_surface(R_s, Z_s, 1)


if __name__ == "__main__":
    main()
