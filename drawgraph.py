import matplotlib.pyplot as plt
from matplotlib import animation
import pickle
import pandas as pd
# 출처 https://jehyunlee.github.io/2021/07/10/Python-DS-80-mpl3d2/

fig, ax = plt.subplots(ncols=1, figsize=(5, 5), subplot_kw={"projection": "3d"})

fontlabel = {"fontsize": "large", "color": "gray", "fontweight": "bold"}
SUFFIX = ('pypy')


def init():

    data_pt = data.pivot_table("time", "calc_amount", "thread")
    X_ = data_pt.columns.tolist()
    Y_ = data_pt.index.tolist()
    X = [X_ for _ in range(len(Y_))]
    Y = [[y_] * len(X_) for y_ in Y_]
    Z = data_pt.values

    ax.set_xlabel("Thread", fontdict=fontlabel, labelpad=16)
    ax.set_ylabel("log_2 Amount", fontdict=fontlabel, labelpad=16)
    ax.set_title("Time", fontdict=fontlabel)

    #ax.scatter(data["x"], data["y"], data["z"],
    #           c=data["z"], cmap="inferno", s=5, alpha=0.5)

    ax.plot_trisurf(data["thread"], data["calc_amount"], data["time"], cmap="hsv")
    ax.contour(X, Y, Z, levels=20, colors="k", linewidths=1)

    return fig,


def animate(i):
    ax.view_init(elev=30., azim=i)
    return fig,


with open(f"point_{SUFFIX}.pkl", "rb") as f: data_pickle = pickle.load(f)
data = pd.DataFrame(data_pickle)

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
# Save
anim.save(f'mpl3d_scatter_{SUFFIX}.gif', fps=30)
data.to_csv(f"point_{SUFFIX}.csv", index=False)