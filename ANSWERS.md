solutions.py has my code, epsilons.png has a plot of the error for the various
methods vs. delta t.

The methods performed, from worst to best, Euler, Midpoint, Euler-Cromer, and
RK4.  RK4 improved the fastest with delta t, Euler-Cromer and Midpoint had
similar orders of improvement to each other, and Euler's improvement started to
flat beyond step counts of 400.

The number of steps and floating point operations used to conserve the energy
to within 1% are below (the Euler method likely wouldn't finish in time to get
0.01% relative error). The number of flops taken are also listed, although this
number assumes an optimal implementation (i.e. things like h/2 are computed
once and not for every timestep).

Euler performed very poorly, taking almost 16,000 steps and nearly 100,000
flops. Euler-Cromer acheived that accuracy with the least amount of flops,
likely because it conserves energy well as a symplectic method. RK4 used the
least amount of steps, but with 4 times as many flops per step it took more
flops. The midpoint method does worse in both step count and flops.
