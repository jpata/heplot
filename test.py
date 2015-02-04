import ROOT
ROOT.gROOT.SetBatch(True)
import heplot as he
from rootpy.plotting import Hist, Hist2D
import matplotlib.pyplot as plt
import random
import matplotlib

#radiator palette
ROOT.gROOT.ProcessLine("gStyle->SetPalette(53, 0);")

#to convert ROOT objects to rootpy objects
from rootpy import asrootpy

tf = ROOT.TFile("test.root", "RECREATE")
tf.cd()

####################################
h1 = ROOT.TH1D("a1", "a", 20, -2, 2) 
h1 = asrootpy(h1)

h2 = ROOT.TH1D("a2", "a", 20, -2, 2) 
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


####################################
# Ratio, 2 histograms
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

tc = ROOT.TCanvas()
h1.Draw()
h2.Draw("SAME")
tc.SaveAs("h2_r.png")

####################################
# 2D histogram
####################################
fig = plt.figure(figsize=(10,8))
ax = plt.axes()

h3 = ROOT.TH2D("h3", "h", 500, -2, 2, 250, -3, 3)
for i in range(1000000):
        h3.Fill(random.gauss(0.5, 0.8), random.gauss(0.0, 1.0))
mat = he.matshow(ax, h3)
fig.colorbar(mat)
fig.tight_layout()
plt.savefig("h3.png")
plt.close()

tc = ROOT.TCanvas("a", "a", 800, 800)
h3.SetStats(False)
h3.Draw("COLZ")
tc.SaveAs("h3_r.png")

tf.Write()
tf.Close()


####################################
# Stack
####################################
fig = plt.figure(figsize=(8,8))
ax1, ax2 = he.ratio_axes(fig)

plt.sca(ax1)
b1 = he.stackhist([h1, h2])
plt.savefig("stack.png")
plt.close()
