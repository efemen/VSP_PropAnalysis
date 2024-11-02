import calc_prop_vlm
import numpy as np

rpm = 5000
U_inf = np.arange(10, 20, 2)
# U_inf = np.array([14])

calc_prop_vlm.prop_calc("./geometry/10x10E-PERF.bem", U_inf, rpm)
