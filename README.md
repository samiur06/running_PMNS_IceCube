# running_PMNS_IceCube

Shared with [arXiv:2511.07541 - Double Bangs in IceCube as a Window to the Neutrino Mass Origin](https://arxiv.org/abs/2511.07541). 

Stores the benchmarks, parameter points, event differences, and the plotting script.

Any mismatch between the leptonic mixing matrices (PMNS matrix) at the production scale and the detection scale can lead to observable differences in neutrino flavor transitions $P_{\alpha\beta}$. We follow the procedure described in [2108.11961](https://arxiv.org/abs/2108.11961) to compute the oscillation probability. 

The free parameters in this model are those that can be chosen randomly at the production scale. These are the atmospheric parameters $\{ \theta_{23}, \Delta m^2_{31}\}$, the CP-odd phases ($\tilde{\alpha}(Q_p^2), \tilde{\beta}(Q_p^2)$, and $\delta(Q_p^2)$), the lightest neutrino mass $m_\nu$, the angles parameterizing the orthogonal $R$ matrix $\{\xi_i\}$, and  the Yukawa matrix $Y_N$, i.e., $\text{diag}(Y_N ^{(1)},Y_N ^{(2)},Y_N ^{(3)})$. $R$ is taken to be a real matrix and parameterized by three Euler-like rotation angles $\xi_1$ in the 1-2 plane, $\xi_2$ in the 2-3 plane, and $\xi_3$ in the 1-3 plane. Each 'parameter point' corresponds a set of these 12 free parameters, namely    
{ $\{\alpha,\beta,\delta,\Delta m^2_{31},\sin^2 \theta_{23},\xi_{1},\xi_{2},\xi_{3}, (Y_N ^{(1)},Y_N ^{(2)},Y_N ^{(3)}),m_1\}$ }.  

Other oscillation parameters are:
$\Delta m_{21} ^2 = 7.49\times 10^{-5} ~\text{eV}^2$, $\sin ^2 \theta_{12} = 0.307$, $\sin ^2 \theta_{13} = 0.02195$ (NuFIT 6.0, 2024)


### benchmarks 
Directory containing benchmark parameter points for Figure 1 and the star benchmark, used in the paper.

### parameter_points
Directory containing parameter points and their sorted order based on the larger average $P_{\mu\tau}$ at high energy.
Two `numpy` array files named `param_n{nmax}_seed{seedX}.npy` contain `nmax` parameter points with random seed `seedX`. Two pair of (`nmax`,`seedX`) are provided; they are $(10000,30)$ and $100000,999$. These integers are associated with random scan of the parameter points, not with physical running. 

The other two `numpy` array files `sorted_mutaulist_{nmax}_seed{seedX}.npy` list the index of each parameter point from the previous array and its corresponding average $P_{\mu\tau}$. The sorted `numpy` array is in descending order with respect to the $\nu_\mu \to \nu_\tau$ conversion, to locate the maximal tau appearance.

### count_diff
Directory containing the differences in events with and without running. The filename structure is `difflist_{nmax}_{seedX}_{srccode}.npy`. These are `numpy` arrays, each element in these arrays has the structure `[nmax, seedX, parameter point index, event_diff_dict]`, where `nmax` and `seedX` are in the filename. `srccode` represents the source flavor composition for the astrophysical neutrinos (e.g., 120 means 1:2:0).  
`event_diff_dict` is a dictionary that has the structure `{det_flavor: ([atmstd, astrostd], [atmrun_nue, atmrun_numu, atmrun_nutau, astrorun], [totalrun - totalstd])}`
- 0,1,2 as `det_flavor` keys to represent the detected flavor e,mu,tau.
- `atmstd` and `astrostd` are the event count of the `det_flavor` (the corresponding key) from atmospheric and astrophysical sources
- `atmrun_nu{incoming_flavor}` and `astrorun` are the event count of the `det_flavor` when running is considered; atmospheric neutrino of flavor `incoming_flavor` converting to `det_flavor`
- `totalstd` $=$ `atmstd` $+$ `astrostd`
- `totalrun` $=$ `atmrun_nue` $+$ `atmrun_numu` $+$ `atmrun_nutau` $+$ `astrorun`
- the last number (`totalrun` $-$ `totalstd`) is the event difference from standard to running for the flavor `det_flavor`  

An example of `event_diff_dict` dictionary is shown below.

`{
  0: ([8.57, 55.54], [7.53, 18.89, 0.00, 54.74], [17.04]),
  1: ([41.68, 11.04], [0.13, 31.12, 0.00, 11.16], [-10.31]),
  2: ([0.00, 2.56], [0.01, 1.32, 0.00, 2.57], [1.33])
}`

We read this as there are no atmospheric tau neutrinos and 2.56 astrophysical tau neutrinos in the standard scenario. When running is considered, there are 0.01, 1.32, 0 tau neutrinos coming from atmospheric electron, muon, and tau neutrinos, respectively (we see dominantly from atm muon neutrino since atm neutrinos are mostly of muon flavor, and furthermore, no tau neutrino in the atm neutrino gives 0 tau neutrino). While tau count from astrophysical sources is 2.57, an increase of only 0.01 from the standard case. Comparing the sums of the standard and running counts, we find an increase of 1.33 events in the running case, the event difference. 

We implement the sorted list of parameter points (`sorted_mutaulist_{nmax}_seed{seedX}.npy`) to select the maximal tau appearance. We choose the top 1000 parameter points from the file of `10000_30` and the top 70 parameter points from the file of `100000_999`, respectively. We compute and provide the event counts and differences for these parameter points. Four different source flavor compositions (`srccode`) were considered. All the results are plotted and shared in the figures. 

### mpl 
Matplotlib style file for the plotting code.

### `plot_count_difference.py`  
The Python script for plotting. It plots the event difference as provided in the `numpy` data files in the **count_diff** directory. It performs the plotting for four different flavor compositions, labeled as the `srccode` in the code. The plots are saved in the **figures** directory. 

### figures
Directory containing all the figures for the four source flavor compositions. The following plot is Figure 2 from the paper, produced using `plot_count_difference.py` with `srccode=120`.  

<img width="767" height="625" alt="image" src="https://github.com/user-attachments/assets/51956b71-057a-422a-b59b-1f6b780046bc" />
