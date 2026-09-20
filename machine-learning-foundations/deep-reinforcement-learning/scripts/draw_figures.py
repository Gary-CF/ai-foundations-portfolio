"""Reproducible mathematical illustrations, not empirical training curves."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'images'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'figure.facecolor':'white','savefig.facecolor':'white'})

def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / (name+'.png'), dpi=180, bbox_inches='tight')
    fig.savefig(OUT / (name+'.svg'), bbox_inches='tight')
    plt.close(fig)

r=np.linspace(0,2,500)
fig, axs=plt.subplots(1,2,figsize=(8.6,3.2))
for ax,a in zip(axs,[2,-2]):
    ax.plot(r,r*a,color='#999999',ls='--',label='unclipped')
    ax.plot(r,np.minimum(r*a,np.clip(r,0.8,1.2)*a),color='#286085',lw=2,label='PPO surrogate')
    ax.axvline(0.8,color='#cccccc',lw=1);ax.axvline(1.2,color='#cccccc',lw=1)
    ax.set(xlabel='probability ratio',ylabel='objective contribution',title=f'Advantage = {a}')
    ax.legend(fontsize=8,loc='best')
save(fig,'ppo-objective')

fig,ax=plt.subplots(figsize=(6.5,3.2))
tau=np.linspace(0.05,0.95,100)
ax.plot(tau,2*tau,color='#286085',lw=2)
ax.scatter([0.5,0.8],[1,1.6],color='#b15c32',zorder=3)
ax.set(xlabel='expectile level',ylabel='expectile value',title='Q = {0, 2}, equal probability',ylim=(0,2))
ax.grid(alpha=.18)
save(fig,'expectile')

fig,ax=plt.subplots(figsize=(6.5,3.2))
for gamma in [.5,.9,.99]:
    k=np.arange(301)
    e=.01*(1-gamma**k)/(1-gamma)
    ax.plot(k,e,label=f'gamma = {gamma}',lw=2)
ax.set(xlabel='backup count',ylabel='value error',title='Fixed local bias = 0.01; one-state MDP')
ax.legend();ax.grid(alpha=.18)
save(fig,'error-amplification')

fig,ax=plt.subplots(figsize=(6.5,3.1))
ax.plot([0,1,2,3,4],[0,1,2.7,2.7,2.7],'o-',label='start state',color='#286085')
ax.plot([0,1,2,3,4],[0,3,3,3,3],'s--',label='branch state',color='#b15c32')
ax.set(xlabel='synchronous value iteration',ylabel='value',xticks=[0,1,2,3,4],title='Reward information propagates backward')
ax.legend();ax.grid(alpha=.18)
save(fig,'value-iteration')
print('Rendered 4 PNG + 4 SVG figures.')
