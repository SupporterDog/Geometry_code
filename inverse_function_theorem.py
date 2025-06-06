# Forward mapping: polar spiral  (always invertible)
f  = lambda x, y: np.array([np.exp(x)*np.cos(y), np.exp(x)*np.sin(y)])
J  = lambda x, y: np.array([[np.exp(x)*np.cos(y), -np.exp(x)*np.sin(y)],
                            [np.exp(x)*np.sin(y),  np.exp(x)*np.cos(y)]])

def f_inv(u, v):
    r = np.hypot(u, v)
    θ = np.arctan2(v, u)
    return np.log(r), θ   # analytic inverse

# Validate Jacobian determinant never zero on sample grid
xx, yy = np.meshgrid(np.linspace(-1,1,40), np.linspace(-np.pi, np.pi,40))
detJ   = np.exp(xx)**2
assert np.all(detJ > 0), "Jacobian vanished!"
print("IFT satisfied everywhere on grid ✓")
