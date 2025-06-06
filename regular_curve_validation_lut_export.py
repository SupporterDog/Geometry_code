import json, time
import numpy as np
from scipy.integrate import quad

# --- 1) Author a helix --------------------------------------------------------
R, h = 1.2, 0.15
alpha  = lambda t: np.array([R*np.cos(t), R*np.sin(t), h*t])
dalpha = lambda t: np.array([-R*np.sin(t), R*np.cos(t), h])
ddalpha = lambda t: np.array([-R*np.cos(t), -R*np.sin(t), 0])

# --- 2) Regularity check ------------------------------------------------------
grid = np.linspace(0, 4*np.pi, 300)
if not np.all(np.linalg.norm([dalpha(t) for t in grid], axis=1) > 1e-6):
    raise ValueError("Curve stalls somewhere!")

# --- 3) Arc length ------------------------------------------------------------
t0 = time.perf_counter()
v   = lambda t: np.linalg.norm(dalpha(t))
arc_len, _ = quad(v, 0, 4*np.pi)
print(f"Arc length: {arc_len:.3f} m  (calc {time.perf_counter()-t0:.3f} s)")

# --- 4) Curvature samples -----------------------------------------------------
kappa = lambda t: np.linalg.norm(np.cross(dalpha(t), ddalpha(t)))/v(t)**3
kappa_samples = [kappa(t) for t in grid]

# --- 5) Build look-up table ---------------------------------------------------
lut = {"t": grid.tolist(),
       "s": (arc_len * np.linspace(0, 1, len(grid))).tolist(),
       "kappa": kappa_samples}
with open("helix_lut.json", "w") as fp:
    json.dump(lut, fp)
print("LUT written → helix_lut.json")
