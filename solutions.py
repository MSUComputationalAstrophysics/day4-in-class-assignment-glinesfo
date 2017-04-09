import numpy as np
import matplotlib.pyplot as plt

def euler(t,u,f,h):
    return u + f(t,u)*h

flopsPerStep_euler = 6

"""
#General EulerCromer
def eulerCromer(t,u,f,h):
    v = u[1] + f(t,u)[1]*h #using x_n
    x = u[0] + f(t,np.array((u[0],v)))[0]*h #using v_n+1
    return np.array((x,v))
"""

#Our Euler Cromer
def eulerCromer(t,u,f,h):
    v = u[1] - k/m*u[0]*h #using x_n
    x = u[0] + v*h #using v_n+1
    return np.array((x,v))

flopsPerStep_eulerCromer = 6


def midpoint(t,u,f,h):
    return u + h*f(t+h/2,u + h/2*f(t,u))

flopsPerStep_midpoint = 15

def rk4(t,u,f,h):
    k1 = f(t,u)
    k2 = f(t+h/2,u+h/2*k1)
    k3 = f(t+h/2,u+h/2*k2)
    k4 = f(t,u+h*k3)
    return u + h/6*(k1 + 2*(k2 + k3) + k4)

flopsPerStep_rk4 = 2+7+7+6+12 


m = 1
k = 1
f = lambda t,u:np.array((u[1],-k/m*u[0]))
u0 = np.array((0,1))

anyl_x = lambda t: np.sin(t)
anyl_v = lambda t: np.cos(t)

Dt = np.array((0.1,0.01,0.001))*np.pi

def epsilon_for_steps(method,steps):
    dt = 4*np.pi/steps
    u = u0.copy()
    t = 0
    e0 = (u[0]**2 + u[1]**2)
    for i in range(steps):
        u = method(t,u,f,dt)
        t += dt
    ef = (u[0]**2 + u[1]**2)
    return np.abs(ef-e0)/e0




for method,name,flops,(si,sf) in zip(
    (euler,eulerCromer,midpoint,rk4),
    ("Euler","Euler-Cromer","Midpoint","RK4"),
    (flopsPerStep_euler,flopsPerStep_eulerCromer,
     flopsPerStep_midpoint,flopsPerStep_rk4),
    ((15870,15880),(40,50),(80,90),(20,30))):

    epsilons = []
    for steps in (40,400,4000):
        epsilons.append(epsilon_for_steps(method,steps))
    plt.loglog(Dt,epsilons,label=name,marker="o")


    epsilons = []
    for steps in np.arange(si,sf):
        epsilons.append(epsilon_for_steps(method,steps))
    epsilons = np.array(epsilons)
    closest = (epsilons < 0.01).argmax()
    print('{0: <10}'.format(name),"\t minimum steps: ",
           closest+si,"\t Flops: ",flops*steps,"\t epsilon: ",epsilons[closest])

plt.legend(loc='best')
plt.savefig("epsilons.png")

plt.show()
