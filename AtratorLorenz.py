import pynamicalsys, numpy as pd, matplotlib.pyplot as plt, seaborn as sns
from pynamicalsys import ContinuousDynamicalSystem as cds
from pynamicalsys import PlotStyler

ds = cds(model = "lorenz system")
ds.intergrator("rk4", time_sleep = 0.005)




parameters = [10, 28, 8/3]    # -- parametros caoticos classicos --
u = [0.1, 0.1, 0.1]    # -- condiçoes iniciais --
tempo_total = 100    # -- tempo total de evoluçao --
trajectory = ds.trajectory(u, tempo_total, parameters = parameters)

print(trajectory.shape)



ps = PlotStyler(fontsize=18, linewidth=0.3)  
ps.apply_style()

plt.plot(trajectory[:, 1], trajectory[:, 3], "k-")

plt.xlabel("$x$")
plt.ylabel("$z$")

plt.show()  
