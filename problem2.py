import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from problem1 import sol, x, y, r

r_val = 10

ellipse_expr = 2*x**2 + 3*y**2 - r
line_expr = y - (2*x + 1)

ellipse_f = sp.lambdify((x, y, r), ellipse_expr, "numpy")
line_f = sp.lambdify((x, y), line_expr, "numpy")

x_vals = np.linspace(-4, 4, 600)
y_vals = np.linspace(-4, 4, 600)
X, Y = np.meshgrid(x_vals, y_vals)

Z1 = ellipse_f(X, Y, r_val)
Z2 = line_f(X, Y)

for s in sol:
    px = float(s[x].subs(r, r_val))
    py = float(s[y].subs(r, r_val))
    plt.plot(px, py, "ro")

plt.contour(X, Y, Z1, levels=[0])
plt.contour(X, Y, Z2, levels=[0])

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.savefig("Problem2.pdf")
plt.close()
