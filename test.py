import ROOT
ROOT.gROOT.SetBatch(True)
import heplot as he
from rootpy.plotting import Hist, Hist2D
import matplotlib.pyplot as plt
import random
import matplotlib

#to convert ROOT objects to rootpy objects
from rootpy import asrootpy

####################################
h1 = ROOT.TH1D("a", "a", 20, -2, 2) 
h1 = asrootpy(h1)

h2 = ROOT.TH1D("a", "a", 20, -2, 2) 
h2 = asrootpy(h2)

for i in range(10000):
    h1.Fill(random.gauss(0, 1))
    h2.Fill(random.gauss(0.2, 0.8))

####################################
fig = plt.figure(figsize=(8,8))
ax = plt.axes()
ax.grid()
b1 = he.barhist(h1, color="red", lw=2)
b2 = he.barhist(h2, color="blue", lw=2)
plt.savefig("h1.png")
plt.close()
####################################

fig = plt.figure(figsize=(8,8))

ax1, ax2 = he.ratio_axes(fig)

plt.sca(ax1)
b1 = he.barhist(h1, color="red", lw=2, label="$ t\\bar{t} + H $")
b2 = he.barhist(h2, color="blue", lw=2, label="$ t\\bar{t} + \\mathrm{jets}$")
plt.legend(loc=2)

plt.sca(ax2)
hratio = h1.Clone("hratio")
hratio.Divide(h2)
bratio = he.barhist(hratio, color="red", lw=2)
plt.axhline(1.0, color="blue", lw=2)

plt.xlabel("$ p_t $ of the leading jet [GeV]")
plt.ylabel("ratio")
plt.savefig("h2.png")
plt.close()
