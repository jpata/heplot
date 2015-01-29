import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt
from rootpy.plotting import Hist, Hist2D
from rootpy.io.file import root_open
import sys
import numpy as np
import matplotlib
import matplotlib.gridspec as gridspec

from matplotlib.ticker import AutoMinorLocator

matplotlib.rc('font', family='sans-serif') 
matplotlib.rc('font', serif='Arial') 
matplotlib.rc('text', usetex='true') 
matplotlib.rcParams.update({'font.size': 16})

def barhist(h, **kwargs):
    col = kwargs.pop("color")

    #b = rplt.errorbar(h, xerr=False, color=col, mec=col, ms=0, ecolor=col, **kwargs)
    lw = kwargs.pop("lw", 1)
    fs = kwargs.pop("fillstyle", False)
    lab = kwargs.pop("label", "")
    kwargs_d = dict(kwargs)
    
    h.fillstyle = "hollow"
    b = rplt.bar(h, lw=0, color="none", ecolor=col, label=None, **kwargs)
    xs = []
    ys = []
    for _b in b:
        xs += [_b.xy[0], _b.xy[0]+_b.get_width()]
        ys += [_b.xy[1]+_b.get_height(), _b.xy[1]+_b.get_height()]
        _b.set_hatch(fs)
        _b.set_color(col)
        plt.gca().add_patch(_b)
    #kwargs_d.pop("lw")
    kwargs_d.pop("edgecolor", "")
    #plt.xticks(np.arange(min(xs), max(xs), (max(xs)-min(xs)) / ))
    plt.plot(xs, ys, color=col, lw=lw, label=lab, **kwargs_d)
    return b

def matshow(ax, hpt, **kwargs):
    return ax.matshow(hpt, cmap="Greys", interpolation="none", origin="lower",
    extent=[hpt.GetXaxis().GetBinLowEdge(1), hpt.GetXaxis().GetBinLowEdge(hpt.GetNbinsX()),
            hpt.GetYaxis().GetBinLowEdge(1), hpt.GetYaxis().GetBinLowEdge(hpt.GetNbinsY())])


def ratio_axes(fig):
    gs = gridspec.GridSpec(2, 1, height_ratios=[2,1])
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax1.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='on',
        top='on',
        width=1, 
        labelbottom='off'  # labels along the bottom edge are off
    )
    ax2.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='on',
        top='on', 
        width=1, 
    )
   
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())

    fig.tight_layout()
    fig.subplots_adjust(hspace=0.02, bottom=0.1, left=0.1, right=0.9, top=0.9)
    #ax2.yaxis.set_ticks_position('right')
    #fig.subplots_adjust(hspace=0.2)
    return ax1, ax2
