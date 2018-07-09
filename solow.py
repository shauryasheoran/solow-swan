
# coding: utf-8

# In[31]:

import numpy as np
from matplotlib import pyplot as plt 


# In[32]:

alpha= 0.2
L_0=10
A_0=1
n=0.1
g=0.1
s=0.2
delta=0.05


# In[33]:

def y(k):
    return pow(k,alpha)
def breakeveninvestment(k):
    return (n+g+delta)*k


# In[34]:

k=np.linspace(0.01,4,51)
plt.subplot(3,1,1)
plt.plot(k,y(k),'b-')
plt.plot(k,s*y(k),'r-')
plt.plot(k,breakeveninvestment(k),'g-')

k_equilibrium= pow(s/(n+g+delta),1/(1-alpha))
plt.plot(k_equilibrium,s*y(k_equilibrium),'bo')

plt.legend(['production per effective-labour','savings per effective-labour','break even investment'],bbox_to_anchor=(1.75,1))
plt.xlabel('capital per effective-labour')
plt.ylabel('production per effective-labour')


# In[35]:

L=[L_0]
A=[A_0]
Y=[]
time_list=[]

time_interval=0.1
time=10
no_of_iterations=int(time/time_interval)

for iter in range(no_of_iterations):
    Y.append(pow(k_equilibrium,alpha)*A[iter]*L[iter])
    L.append(L[iter]+L[iter]*n*time_interval)
    A.append(A[iter]+A[iter]*g*time_interval)
    time_list.append(iter*time_interval)
    


# In[36]:
plt.subplot(3,1,2)
plt.plot(time_list,Y)
plt.xlabel('time')
plt.ylabel('Production')


# In[37]:

n_new=0.05
g_new=0.1
s_new=0.3


# In[38]:

k=[k_equilibrium,k_equilibrium]
L=[L_0]
A=[A_0]
time_list=[0,1]
production_per_capita=[y(k_equilibrium),y(k_equilibrium)]
time_interval=0.1
time=10
no_of_iterations=int(time/time_interval)
for iter in range(no_of_iterations):
    L.append(L[iter]+L[iter]*n_new*time_interval)
    A.append(A[iter]+A[iter]*g_new*time_interval)
    k.append(k[iter+1]+(s_new*production_per_capita[iter+1]-(n_new+g_new+delta)*k[iter+1])*time_interval )
    production_per_capita.append(y(k[iter+1]))
    time_list.append(iter*time_interval+1)


# In[39]:

k_new_equilibrium= pow(s_new/(n_new+g_new+delta),1/(1-alpha))
plt.subplot(3,1,3)
plt.plot(time_list,production_per_capita)
plt.plot([0,time_list[-1]],[y(k_new_equilibrium),y(k_new_equilibrium)],'r-')
plt.xlabel('time')
plt.ylabel('Production per effective labour')
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



