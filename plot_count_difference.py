import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.style
matplotlib.style.use("./mpl/paper.mplstyle")

# srccode is the source flavor ratio, for astrophysical neutrinos 
for srccode in ['010', '100', '110', '120']:

    # Load the array: corresponding to two sets of benchmarks 
    # '10000_30' has 1000 benchmarks 
    nmax   = 10000
    seedX  = 30
    path = f"count_diff/difflist_{nmax}_{seedX}_{srccode}.npy"
    data10K = np.load(path, allow_pickle=True)     # shape: (N, 2) where second element itself has 3 entries
    print('np.shape(data10)=',np.shape(data10K))

    # '1000000_999' has 70 benchmarks 
    nmax   = 100000
    seedX  = 999
    path = f"count_diff/difflist_{nmax}_{seedX}_{srccode}.npy"
    data100K = np.load(path, allow_pickle=True)     # shape: (N, 2) where second element itself has 3 entries
    print('np.shape(data100)=',np.shape(data100K))

    data = np.concatenate((data10K, data100K), axis=0)
    print('np.shape(data)=', np.shape(data))

    delta_mu  = [d[-1][1][-1][-1] for d in data]
    delta_tau = [d[-1][2][-1][-1] for d in data]

    # Scatter plot
    plt.figure(figsize=(6,5))
    plt.scatter(delta_mu, delta_tau, s=15, color="green", alpha=0.7, marker='D')
    # star benchmark index: 1000 in regular (0-999), and 1st benchmark in the top70 list- 1000 -th location
    plt.scatter([delta_mu[1000]], [delta_tau[1000]], s=100, color="black", alpha=1., marker='*')
    plt.xlabel(r'$\Delta N_{\mu}$')
    plt.ylabel(r'$\Delta N_{\tau}$')
    plt.xlim(-18,2)
    plt.ylim(-0.3,2.7)
    plt.tick_params(
        top=True, bottom=True, left=True, right=True,
        which='both',         # apply to major and minor ticks
        direction='in',       # optional: draw ticks inward
        labeltop=False, labelbottom=True,
        labelleft=True, labelright=False
    )

    src_text = rf'$\nu_e:\nu_\mu:\nu_\tau = {"{:s}".format(":".join(srccode))}$'
    plt.text(
    0.95, 0.91, src_text,
    transform=plt.gca().transAxes,
    ha='right', va='top',
    fontsize=16, fontweight='bold', color='black')
    plt.minorticks_on()
    plt.tight_layout()
    plt.savefig(f"figures/count_difference_src{srccode}.pdf",dpi=400)
    plt.show()
