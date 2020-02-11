
# coding: utf-8

# In[1]:


import random

def slot_machine():
    symbols = ['lemon','grapes','sevens','oranges','gold bar','cherries', 'cash']*4+ ['WIN']*2
    result = [random.choice(symbols) for i in range(4)]
    if(result[0] == result[1] and result[1] == result[2] and result[2] == result[3]):
        if('WIN' in result):
          return 'Win 50X!'
        return 'Win 20X!'
    elif(result.count('WIN') > 2):
        return 'Win 10X!'
    elif(result[0] == result[3] and result[1] == result[2]):
        if('WIN' in result):
          return 'Win 5X!'
        return 'Win 2X!'
    return 'Lose!'
    

def slot_machine_2():
    symbols = ['lemon','grapes','sevens','oranges','gold bar','cherries', 'cash']*4+ ['WIN']*2
    result = [symbols[random.randint(0,29)]]*4
    if(result[0] == result[1] and result[1] == result[2] and result[2] == result[3]):
        if('WIN' in result):
          return 'Win 50X!'
        return 'Win 20X!'
    elif(result.count('WIN') > 2):
        return 'Win 10X!'
    elif(result[0] == result[3] and result[1] == result[2]):
        if('WIN' in result):
          return 'Win 5X!'
        return 'Win 2X!'
    return 'Lose!'


def marbles():
  marbs = ['R']*15 + ['B']*10
  result = [random.choice(marbs), random.choice(marbs), random.choice(marbs), random.choice(marbs)]
  if('R' not in result):
    return 'Win all blue!'
  elif result == ['B','B','R','R']:
    return 'Win second combo!'
  
  
def test_probs(repetitions, func):
    result = [func() for i in range(repetitions)]
    return {k:result.count(k) for k in result}
    

print(test_probs(10000, marbles))
print(test_probs(100000, slot_machine))


# In[2]:


lose_count = 0
win_50 = 0
win_20 = 0
win_10 = 0
win_5 = 0
win_2 = 0

for i in range(10000):
    result = slot_machine()
    if result == "Win 50X!":
        win_50 += 1
    elif result == "Win 20X!":
        win_20 += 1
    elif result == "Win 10X!":
        win_10 += 1
    elif result == "Win 5X!":
        win_5 += 1
    elif result == "Win 2X!":
        win_2 += 1
    else:
        lose_count += 1


# In[3]:


win_50


# In[4]:


win_20


# In[5]:


win_10


# In[6]:


win_5


# In[7]:


win_2


# In[8]:


lose_count


# In[9]:


twolose_count = 0
twowin_50 = 0
twowin_20 = 0
twowin_10 = 0
twowin_5 = 0
twowin_2 = 0

for i in range(10000):
    result = slot_machine_2()
    if result == "Win 50X!":
        twowin_50 += 1
    elif result == "Win 20X!":
        twowin_20 += 1
    elif result == "Win 10X!":
        twowin_10 += 1
    elif result == "Win 5X!":
        twowin_5 += 1
    elif result == "Win 2X!":
        twowin_2 += 1
    else:
        twolose_count += 1


# In[10]:


twolose_count


# In[11]:


twowin_50


# In[12]:


twowin_20


# In[13]:


twowin_10


# In[14]:


twowin_5


# In[15]:


twowin_2


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss
import matplotlib.pyplot as plt
import math


# In[17]:


crashData = pd.read_csv("Police_Crash_Reports_2016.csv")


# In[18]:


crashData


# In[19]:


crashes_Info = crashData.groupby(crashData["Precinct"])


# In[20]:


crashes_Info.describe()


# In[21]:


prec2_Info = crashData.loc[crashData["Day of Week"].str.startswith("S") & (crashData["Precinct"] == 2)]


# In[22]:


prec2_Info.shape


# In[23]:


prec4_Info = crashData.loc[(crashData["Day of Week"] == ("TUE")) & (crashData["Precinct"] == 4)]


# In[24]:


prec4_Info.shape


# In[25]:


prec3_Info = crashData.loc[(crashData["Day of Week"] == ("FRI")) & (crashData["Precinct"] == 3)]


# In[26]:


prec3_Info.shape


# In[28]:


1-ss.poisson(5).cdf(10)


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import pandas as pd
from scipy.stats import binom, norm


distn = pd.Series(index = range(401),data =[binom.pmf(i, 400, 0.4) for i in range(401)])
sns.barplot(x = distn.index, y = distn.values)


# In[34]:


fourtyPercent = .4*400
print(fourtyPercent)


# In[35]:



print(binom.pmf(150,400,0.4))


# In[90]:


print(1 - binom.cdf(149,400,0.4))


# In[40]:


norm.fit(binom.pmf(150,400,0.4))


# In[41]:


conData = pd.read_csv("congress-terms.csv")


# In[42]:


conData


# In[64]:


con_105 = (conData['congress'] == 105)


# In[69]:


sns.distplot(conData['age'][conData['congress'] == 105], kde=False)


# In[70]:


norm.fit(conData['age'][conData['congress'] == 105])


# In[71]:


(conData['age'][conData['congress'] == 105]).describe()


# In[72]:


mu = 53.082904
sigma = 9.998227


# In[98]:


1 - norm.cdf(75, mu, sigma)


# In[74]:


norm.cdf(50,mu,sigma) -norm.cdf(40, mu, sigma)


# In[76]:


norm.ppf(0.24, mu, sigma)


# In[77]:


norm.ppf(0.76, mu, sigma)


# In[91]:


con_105 = conData[conData['congress'] == 105]
great_75 = con_105[con_105['age'] > 75]
great_75.shape[0]/con_105.shape[0]


# In[92]:


con_105 = conData[conData['congress'] == 105]
betw = conData[(conData['congress'] == 105) & (conData['age']).between(40, 50)]
betw.shape[0]/con_105.shape[0]


# In[93]:


con_105.describe()


# In[94]:


con_105


# In[97]:


congressAge = np.percentile(con_105['age'], 24)
print(congressAge)

