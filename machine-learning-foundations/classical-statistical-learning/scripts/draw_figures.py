"""Reproduce exact mathematical diagrams; requires numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'images'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','savefig.facecolor':'white'})
blue='#27628e'; red='#b24b40'; gray='#64727d'; green='#34775b'
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=210,bbox_inches='tight')
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight')
    plt.close(fig)
def axes0(ax,xlabel,ylabel):
    ax.axhline(0,color='#999999',lw=.8); ax.axvline(0,color='#999999',lw=.8)
    ax.set_xlabel(xlabel);ax.set_ylabel(ylabel)

fig,ax=plt.subplots(figsize=(7,3.7),layout='constrained')
ax.plot([-0.4,3.4],[0,0],color=blue,lw=2)
ax.annotate('',(2,2),(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':gray})
ax.annotate('',(2,0),(0,0),arrowprops={'arrowstyle':'->','lw':3,'color':blue})
ax.annotate('',(2,2),(2,0),arrowprops={'arrowstyle':'->','lw':2,'color':red})
ax.plot([1.82,1.82,2],[0,.18,.18],color=gray)
ax.text(2.12,2,r'$Y$',fontsize=14);ax.text(1.75,-.36,r'$\hat Y=PY$',fontsize=13)
ax.text(2.12,1,r'$e=Y-\hat Y$',fontsize=13);ax.text(2.55,.15,r'$\mathrm{Col}(X)$')
ax.text(-.12,-.25,'0');ax.set_xlim(-.5,3.6);ax.set_ylim(-.5,2.4);ax.set_aspect('equal');ax.axis('off');save(fig,'01-projection')

rng=np.random.default_rng(17)
p0=rng.normal(size=(18,2))*[.24,.35]+[-1.25,-.15]
p1=rng.normal(size=(18,2))*[.24,.35]+[1.25,.15]
fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained')
for ax,w,title in zip(axs,[np.array([0,1]),np.array([1,0])],['Weak separation','Strong separation']):
    for p,c,m in [(p0,blue,'o'),(p1,red,'x')]:
        ax.scatter(*p.T,c=c,marker=m,s=23,alpha=.8)
        proj=np.outer(p@w,w)
        for a,b in zip(p,proj):ax.plot([a[0],b[0]],[a[1],b[1]],color=c,alpha=.13,lw=.7)
        ax.scatter(*proj.T,c=c,marker=m,s=30)
    ax.plot([-2*w[0],2*w[0]],[-2*w[1],2*w[1]],color=gray,lw=1)
    ax.set_title(title);ax.set_xlim(-2.05,2.05);ax.set_ylim(-1.6,1.6);ax.set_aspect('equal');ax.set_xlabel('$x_1$');ax.set_ylabel('$x_2$')
save(fig,'01-fisher')

fig,ax=plt.subplots(figsize=(6.3,4),layout='constrained')
for x,style in [(0,'-'),(-1,'--'),(1,'--')]:ax.axvline(x,color=gray,lw=1.5,ls=style)
neg=np.array([[-1,-.6],[-1.6,.8],[-2,-.9],[-1.5,0]])
pos=np.array([[1,.7],[1.6,-.8],[2,.4],[1.8,1.1]])
ax.scatter(*neg.T,c=blue,s=45,marker='o',label='$y=-1$');ax.scatter(*pos.T,c=red,s=50,marker='x',label='$y=+1$')
ax.scatter([-1,1],[-.6,.7],facecolors='none',edgecolors=gray,s=180)
ax.annotate('',(-1,-1.25),(1,-1.25),arrowprops={'arrowstyle':'<->','color':gray})
ax.text(0,-1.52,r'$2/\|w\|$',ha='center');ax.text(0,1.4,r'$w^\top x+b=0$',ha='center');ax.set_ylim(-1.7,1.65);ax.set_xlim(-2.5,2.5);ax.set_xlabel('$x_1$');ax.set_ylabel('$x_2$');ax.legend(loc='upper left');save(fig,'02-svm-margin')

fig,ax=plt.subplots(figsize=(6.6,4),layout='constrained')
x=np.linspace(-1.45,1.6,100);ax.axvspan(-1.5,0,color=blue,alpha=.06)
ax.plot(x,1-x,color=green,label=r'$t=1-u\quad(\lambda=1)$')
ax.scatter([-1,0,1],[2,2,0],color=blue,s=60,zorder=5)
ax.scatter([0],[1],color=green,s=55,zorder=5)
ax.annotate('$p^*=2$',(0,2),(.3,2.3),arrowprops={'arrowstyle':'-','color':gray})
ax.annotate('$d^*=1$',(0,1),(.4,1.3),arrowprops={'arrowstyle':'-','color':gray})
ax.text(-1.35,2.8,r'Feasible side: $u\leq0$',fontsize=10)
axes0(ax,'Constraint value $u$','Objective value $t$');ax.set_xlim(-1.5,1.6);ax.set_ylim(-.3,3.1);ax.legend(loc='upper right',fontsize=9);save(fig,'02-duality-gap')

fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
ax=axs[0];u=np.linspace(-1.2,2.3,250)
ax.axvspan(-1.2,0,color=blue,alpha=.06);ax.plot(u,(u-1)**2,color=blue,label=r'$t=(u-1)^2$');ax.plot(u,1-2*u,color=green,ls='--',label=r'$t=1-2u$')
ax.scatter([-1,0],[4,1],color=[blue,red],s=50,zorder=5)
ax.annotate('Strictly feasible',(-1,4),(-.75,4.7),arrowprops={'arrowstyle':'->','color':gray},fontsize=10)
ax.annotate('$p^*=d^*=1$',(0,1),(.5,2.1),arrowprops={'arrowstyle':'->','color':gray})
axes0(ax,'$u=x$','$t=f(x)$');ax.set_xlim(-1.2,2.3);ax.set_ylim(-.3,5.1);ax.legend(loc='upper right',fontsize=9)
ax=axs[1];l=np.linspace(0,4.3,200);ax.plot(l,l-l*l/4,color=green);ax.scatter([2],[1],color=red,zorder=5)
ax.axhline(1,color=gray,ls=':',lw=1);ax.annotate(r'$\lambda^*=2$',(2,1),(2.6,.73),arrowprops={'arrowstyle':'->','color':gray})
ax.set_title(r'$q(\lambda)=\lambda-\lambda^2/4$');ax.set_xlabel(r'$\lambda$');ax.set_ylabel('Dual lower bound');ax.set_ylim(-.4,1.18);save(fig,'02-slater')

fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
ax=axs[0];t=np.linspace(-1.5,1.5,300);ax.plot(t*t,t,color=blue,label=r'$G=\{(x^2,x)\}$')
u=np.linspace(-.2,2.3,300)
for l,ls in [(.5,':'),(1,'--'),(3,'-')]:ax.plot(u,-l*u-1/(4*l),ls=ls,color=green,alpha=.8,label=rf'$\lambda={l}$')
ax.scatter([0],[0],color=red,s=45,zorder=5);ax.text(.13,.15,r'$p^*=0$');axes0(ax,'$u=x^2$','$t=x$');ax.set_xlim(-.2,2.3);ax.set_ylim(-1.55,1.55);ax.legend(loc='upper right',fontsize=9)
ax=axs[1];l=np.linspace(.12,12,250);ax.plot(l,-1/(4*l),color=green);ax.axhline(0,color=red,ls='--');ax.text(4,.05,r'$d^*=0$ (not attained)',color=red);ax.set_ylim(-1.2,.2);ax.set_xlabel(r'$\lambda$');ax.set_ylabel(r'$q(\lambda)$');ax.set_title(r'$q(\lambda)=-1/(4\lambda)$');save(fig,'02-no-slater')

rng=np.random.default_rng(7);p=rng.normal(size=(38,2))*[1.5,.32];a=.53;rot=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]]);p=p@rot.T;p-=p.mean(axis=0);w=np.linalg.svd(p,full_matrices=False)[2][0];proj=np.outer(p@w,w)
fig,ax=plt.subplots(figsize=(6.8,4),layout='constrained');ax.scatter(*p.T,c=blue,s=22)
for v,q in zip(p,proj):ax.plot([v[0],q[0]],[v[1],q[1]],c=gray,alpha=.3,lw=.7)
ax.plot([-3*w[0],3*w[0]],[-3*w[1],3*w[1]],c=red,lw=2,label='First principal direction');ax.scatter(*proj.T,c=red,s=12,alpha=.6);ax.set_aspect('equal');ax.set_xlabel('$x_1$');ax.set_ylabel('$x_2$');ax.legend(fontsize=9);save(fig,'03-pca')

def node(ax,p,label,color=blue,r=.19):
    ax.add_patch(Circle(p,r,fc='white',ec=color,lw=1.6,zorder=3));ax.text(*p,label,ha='center',va='center',fontsize=12,zorder=4)
def edge(ax,a,b,directed=True):
    a=np.array(a);b=np.array(b);v=(b-a)/np.linalg.norm(b-a);a=a+.20*v;b=b-.20*v
    ax.annotate('',b,a,arrowprops={'arrowstyle':'->' if directed else '-','lw':1.4,'color':gray},zorder=1)
def setup(ax,title):
    ax.set_xlim(-.5,2.5);ax.set_ylim(-.5,1.6);ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontsize=11)
fig,axs=plt.subplots(1,3,figsize=(10,3),layout='constrained')
pos=[(0,.4),(1,.4),(2,.4)]
for ax,title,arcs in zip(axs,['Chain','Fork','Collider'],[[(0,1),(1,2)],[(1,0),(1,2)],[(0,1),(2,1)]]):
    setup(ax,title)
    for p,l in zip(pos,['$A$','$B$','$C$']):node(ax,p,l)
    for i,j in arcs:edge(ax,pos[i],pos[j])
    ax.text(1,-.25,r'$A\perp C\mid B$' if title!='Collider' else r'$A\perp C$',ha='center')
save(fig,'08-dag-motifs')
fig,axs=plt.subplots(1,3,figsize=(10,3.4),layout='constrained')
pos=[(0,1),(1,0),(2,1)]
for ax,title in zip(axs,['DAG','Moral graph','One joint factor']):setup(ax,title)
for p,l in zip(pos,['$A$','$B$','$C$']):
    for ax in axs:node(ax,p,l)
edge(axs[0],pos[0],pos[1]);edge(axs[0],pos[2],pos[1])
for i,j in [(0,1),(1,2),(0,2)]:edge(axs[1],pos[i],pos[j],False)
f=(1,.8);axs[2].add_patch(Rectangle((.88,.68),.24,.24,fc=gray,zorder=4));axs[2].text(1,1.12,'$f(A,B,C)$',ha='center',fontsize=10)
for p in pos:edge(axs[2],p,f,False)
save(fig,'08-moral-factor')
fig,ax=plt.subplots(figsize=(9,3),layout='constrained')
for i in range(4):
    node(ax,(i,1),rf'$z_{i+1}$');node(ax,(i,0),rf'$o_{i+1}$',gray)
    edge(ax,(i,1),(i,0))
    if i<3:edge(ax,(i,1),(i+1,1))
ax.set_xlim(-.4,3.4);ax.set_ylim(-.4,1.4);ax.set_aspect('equal');ax.axis('off');save(fig,'09-hmm')
fig,ax=plt.subplots(figsize=(9,2.8),layout='constrained')
for i in range(4):
    node(ax,(i,0),rf'$y_{i+1}$')
    if i<3:edge(ax,(i,0),(i+1,0),False);ax.text(i+.5,.22,rf'$\psi_{i+2}$',ha='center',color=gray)
ax.add_patch(Rectangle((-.25,.72),3.5,.45,fc='#edf2f6',ec='none'));ax.text(1.5,.94,r'Conditioned on the full input $x_{1:T}$',ha='center',fontsize=11)
ax.set_xlim(-.4,3.4);ax.set_ylim(-.4,1.3);ax.set_aspect('equal');ax.axis('off');save(fig,'10-crf')
print('Created 11 diagrams in PNG and SVG.')
