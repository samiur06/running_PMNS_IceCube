# running_PMNS_IceCube
Stores the benchmarks, difference, and code for event difference plot.

Any mismatch between the mixing matrices at the production scale and the detection scale can lead to observable difference in flavor transition $P_{\alpha\beta}$.  
We follow the procedure described in [arxiv:2108.11961](https://arxiv.org/abs/2108.11961) in order to compute the oscillation probability. 

The free parameters in this model are the parameters that can be chosen at random at the production scale. These are the atmospheric parameters $\{ \theta_{23}, \Delta m^2_{31}\}$, the CP-odd phases $\tilde{\alpha}(Q_p^2), \tilde{\beta}(Q_p^2)$ and $\delta(Q_p^2)$, lightest neutrino mass $m_\nu$, the angles parameterizing the orthogonal $R$ matrix $\{\xi_i\}$,  the Yukawa matrix $Y_N$ to be $\text{diag}(Y_N ^{(1)},Y_N ^{(2)},Y_N ^{(3)})$. We will assume $R$ to be real and parameterized by three Euler-like rotation angles $\xi_1$ in 1-2 plane, $\xi_2$ in 2-3 plane and $\xi_3$ in 1-3 plane. 

Each 'parameter point' is a set of these 12 free parameters, namely $\{     \alpha,\beta,\delta,\Delta m^2_{31},\sin^2 \theta_{23},\xi_{1},\xi_{2},\xi_{3}, (Y_N ^{(1)},Y_N ^{(2)},Y_N ^{(3)}),m_1 \}$.  
