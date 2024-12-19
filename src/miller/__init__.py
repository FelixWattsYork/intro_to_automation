from numpy import pi, cos, sin, arcsin, linspace
import matplotlib.pyplot as plt
import os
import argparse

def plot_surface(R_s, Z_s, savefig,name,ax=None):
    """
    Help on funciton plot_surface in module mille.py

    plots a flux surface in 2d
    """
    if ax is not None:
       ax = plt.subplot2grid((3, 3), (0, 0), colspan=2)
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig:
        plt.savefig(os.getcwd() + "/" + name)
    return ax


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

    parser = argparse.ArgumentParser(
    prog="Miller",
    description="Plots a flux surface",
    epilog="Text at the bottom of help",
    )

    parser.add_argument("A", type=float,help="A value")
    parser.add_argument("kappa", type=float, help = "kappa value")
    parser.add_argument("delta", type=float, help = "delta value")
    parser.add_argument("R0", type=float, help = "R0 Value")
    parser.add_argument("-s", "--save", action="store_true")  # on/off flag
    parser.add_argument("-o", "--output", type=str, default="miller.png", help="Output file name")

    args = parser.parse_args()
    A, kappa, delta, R0,savefile,file_name = args.A, args.kappa,args.delta,args.R0,args.save,args.output
    print(A, kappa, delta, R0,savefile,file_name)

    R_s, Z_s = flux_surface(A, kappa, delta, R0)
    plot_surface(R_s, Z_s, savefile,file_name)


if __name__ == "__main__":
    main()
