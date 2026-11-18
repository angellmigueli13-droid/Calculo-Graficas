"""
Parcial Tercer Corte - Calculo Vectorial (Version C)
Graficas del punto 1 (paralelogramo R) y del punto 2 (tetraedro E).
Requiere: numpy, matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------------------------------------------------------------
# PUNTO 1: paralelogramo R limitado por x-y=0, x-y=2, x+2y=1, x+2y=4
# ---------------------------------------------------------------
def punto1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Plano xy
    x = np.linspace(-1, 4, 400)
    ax1.plot(x, x, "r", label="x - y = 0")
    ax1.plot(x, x - 2, "darkorange", label="x - y = 2")
    ax1.plot(x, (1 - x) / 2, "b", label="x + 2y = 1")
    ax1.plot(x, (4 - x) / 2, "purple", label="x + 2y = 4")

    V = np.array([[1/3, 1/3], [5/3, -1/3], [8/3, 2/3], [4/3, 4/3]])
    ax1.fill(V[:, 0], V[:, 1], color="teal", alpha=0.3, label="R")
    etiquetas = ["(1/3, 1/3)", "(5/3, -1/3)", "(8/3, 2/3)", "(4/3, 4/3)"]
    for (vx, vy), t in zip(V, etiquetas):
        ax1.plot(vx, vy, "ko")
        ax1.annotate(t, (vx, vy), textcoords="offset points", xytext=(6, 6))

    ax1.axhline(0, color="k", lw=0.8)
    ax1.axvline(0, color="k", lw=0.8)
    ax1.set_xlim(-0.5, 3.5)
    ax1.set_ylim(-1.5, 2.5)
    ax1.set_aspect("equal")
    ax1.grid(alpha=0.3)
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Region R en el plano xy")
    ax1.legend(loc="upper left", fontsize=8)

    # Plano uv
    ax2.fill([0, 2, 2, 0], [1, 1, 4, 4], color="teal", alpha=0.3, label="S")
    for p in [(0, 1), (2, 1), (2, 4), (0, 4)]:
        ax2.plot(*p, "ko")
        ax2.annotate(str(p), p, textcoords="offset points", xytext=(6, 6))
    ax2.axhline(0, color="k", lw=0.8)
    ax2.axvline(0, color="k", lw=0.8)
    ax2.set_xlim(-0.5, 3)
    ax2.set_ylim(-0.5, 5)
    ax2.set_aspect("equal")
    ax2.grid(alpha=0.3)
    ax2.set_xlabel("u = x - y")
    ax2.set_ylabel("v = x + 2y")
    ax2.set_title("Region S en el plano uv: 0<=u<=2, 1<=v<=4")
    ax2.legend(loc="upper left", fontsize=8)

    fig.suptitle("Punto 1  |  J = 1/3,  integral = 5,  area(R) = 2")
    fig.tight_layout()
    fig.savefig("punto1_paralelogramo.png", dpi=150)


# ---------------------------------------------------------------
# PUNTO 2: tetraedro E limitado por los planos coordenados y x+y+z=2
# ---------------------------------------------------------------
def punto2():
    O, A, B, C = [0, 0, 0], [2, 0, 0], [0, 2, 0], [0, 0, 2]

    fig = plt.figure(figsize=(12, 5.5))

    ax = fig.add_subplot(1, 2, 1, projection="3d")
    caras = [[O, A, B], [O, A, C], [O, B, C], [A, B, C]]
    colores = ["lightgray", "lightgray", "lightgray", "teal"]
    ax.add_collection3d(Poly3DCollection(caras, facecolors=colores,
                                         edgecolors="k", alpha=0.35))
    ax.add_collection3d(Poly3DCollection([[O, A, B]], facecolors="orange",
                                         alpha=0.5))
    for p, t in zip([O, A, B, C], ["(0,0,0)", "(2,0,0)", "(0,2,0)", "(0,0,2)"]):
        ax.scatter(*p, color="k")
        ax.text(*p, " " + t)
    ax.scatter(0.5, 0.5, 0.5, color="red", s=40)
    ax.text(0.5, 0.5, 0.5, "  centroide", color="red")
    ax.set_xlim(0, 2.3)
    ax.set_ylim(0, 2.3)
    ax.set_zlim(0, 2.3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.view_init(elev=22, azim=40)
    ax.set_title("Tetraedro E: x + y + z = 2")

    ax2 = fig.add_subplot(1, 2, 2)
    x = np.linspace(0, 2, 100)
    ax2.fill_between(x, 0, 2 - x, color="orange", alpha=0.4, label="D: 0<=y<=2-x")
    ax2.plot(x, 2 - x, "k", label="y = 2 - x")
    for p in [(0, 0), (2, 0), (0, 2)]:
        ax2.plot(*p, "ko")
        ax2.annotate(str(p), p, textcoords="offset points", xytext=(6, 6))
    ax2.set_xlim(-0.3, 2.6)
    ax2.set_ylim(-0.3, 2.6)
    ax2.set_aspect("equal")
    ax2.grid(alpha=0.3)
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_title("Proyeccion de E en el plano xy")
    ax2.legend(fontsize=8)

    fig.suptitle("Punto 2  |  V = 4/3,  integral de y dV = 2/3,  y barra = 1/2")
    fig.tight_layout()
    fig.savefig("punto2_tetraedro.png", dpi=150)


if _name_ == "_main_":
    punto1()
    punto2()
    plt.show()