import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401

xyz = np.array([alpha(t) for t in grid])
fig = plt.figure(figsize=(6, 5))
ax  = fig.add_subplot(111, projection="3d")
ax.plot(*xyz.T, lw=2)
ax.set_title("Helix – regular curve")
ax.set_box_aspect((1,1,0.5))
plt.show()
