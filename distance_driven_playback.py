# Assume 'lut' loaded from JSON
import bisect

class CurvePlayer:
    def __init__(self, lut):
        self.t = np.array(lut["t"])
        self.s = np.array(lut["s"])
        self.k = np.array(lut["kappa"])
        self.L = self.s[-1]
        # Helper for interpolation
        self._interp = lambda arr, idx, lam: arr[idx]*(1-lam) + arr[idx+1]*lam
    
    def eval(self, s_query):
        """Return position & curvature at travelled distance s_query."""
        s_query = np.clip(s_query, 0, self.L)
        idx = bisect.bisect_left(self.s, s_query) - 1
        lam = (s_query - self.s[idx]) / (self.s[idx+1] - self.s[idx])
        t   = self._interp(self.t, idx, lam)
        pos = alpha(t)
        curv= self._interp(self.k, idx, lam)
        return pos, curv

# --- demo “game loop” ---------------------------------------------------------
player = CurvePlayer(lut)

speed_mps   = 5.0       # constant 5 m s⁻¹ dash
trail_thrsh = 0.4       # show FX when κ > 0.4
dt          = 1/60.0    # 60 Hz

s_travelled = 0.0
for frame in range(int(player.L/speed_mps/dt)):
    pos, κ = player.eval(s_travelled)
    if κ > trail_thrsh:
        print(f"frame {frame:04d}: Trail ON  κ={κ:.3f}")
    s_travelled += speed_mps * dt
