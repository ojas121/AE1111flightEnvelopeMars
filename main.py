import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


def vmin(weightvm, area, mdensities, clvm):
    vmins = []
    for densityvm in mdensities:
        vsquared = np.divide(weightvm * 2, area * densityvm * clvm)
        velocity = np.sqrt(vsquared)
        vmins.append(velocity)
    return vmins


# def pr(weight, coefficientd, density, area, coefficientl):
#     num = np.multiply(np.multiply(weight ** 3, coefficientd ** 2), 2)
#     den = np.multiply(np.multiply(density, area), coefficientl ** 3)
#     prs = np.sqrt(np.divide(num, den))
#     return prs


fig, ax1 = plt.subplots(1, 1)

plt.xlabel("Velocity [$m/s$]")
plt.ylabel("Altitude [$km$]")

heights = np.arange(0, 52000, 1000)
densities = [0.015029862983125,
             0.013793119363514,
             0.012658359014765,
             0.011617156141171,
             0.010661782292547,
             0.009785148558118,
             0.00898075255918,
             0.008242629841635,
             0.007636285042305,
             0.007046484045304,
             0.006502844607231,
             0.006001718701576,
             0.006001718701576,
             0.005539748806117,
             0.005113844624499,
             0.00472116168291,
             0.004359081650122,
             0.004025194241519,
             0.003717280579048,
             0.003433297889389,
             0.003171365432245,
             0.002929751559389,
             0.002706861813154,
             0.002501227980494,
             0.002311498025507,
             0.002136426829567,
             0.001974867673965,
             0.001825764405202,
             0.001688144227967,
             0.001561111075216,
             0.001443839508929,
             0.001335569108829,
             0.001235599309806,
             0.001143284651989,
             0.001058030410286,
             0.000979288572915,
             0.000906554140893,
             0.000839361722734,
             0.000777282400657,
             0.000719920846535,
             0.000666912667565,
             0.000617921963249,
             0.000572639076767,
             0.000530778525173,
             0.000492077094109,
             0.000456292083881,
             0.000423199694787,
             0.000392593540586,
             0.000364283279859,
             0.000338093355859,
             0.000313861836193,
             0.000291439344378]
clmax = 1.340471
mass = 12
span = 3*2
chord = 0.15/2

s = span * chord
w = mass * 3.71

minVs = vmin(w, s, densities, clmax)

pa = 274.92
cl = 0.004286
cd = 0.012400085888479


cdmax = 0.058003

# prs = pr(w, cd, densities, s, cl)
vmaxs = []
for density in densities:
    velocities = np.arange(110, 1000, 0.5)
    vcubed = np.multiply(np.square(velocities), velocities)
    pr = np.multiply(0.5 * density * s * cd, vcubed)
    vmax = np.argwhere(np.diff(np.sign(pa - pr))).flatten()
    vmaxs.append(vmax[0])

vliftmins = []
for density in densities:
    velocities = np.arange(110, 1000, 0.5)
    lift = np.multiply(0.5*density*s*clmax, np.square(velocities))
    weight = w
    vmaxlift = np.argwhere(np.diff(np.sign(lift - weight))).flatten()
    if vmaxlift.size == 0:
        vliftmins.append(0)
    else:
        vliftmins.append(vmaxlift[0])

# vs = np.arange(0, 52, 1)

plt.plot(minVs, heights, label="Stall speed", linestyle="dashdot")
plt.plot(vmaxs, heights,linestyle="dotted", label="Maximum speed")
plt.plot(vliftmins, heights, "--", label="Minimum lift")
plt.plot([0, 1200], [34000, 35000], label="Service ceiling")
plt.legend()
plt.title("Flight Envelope Mars")
ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000))
ax1.yaxis.set_major_formatter(ticks)
ax1.annotate("Flight envelope", xy=(195, 8000), xytext=(300, 7000), arrowprops=dict(arrowstyle="->", facecolor='black'))
# ax1.set_xlim(right=700)
plt.show()
