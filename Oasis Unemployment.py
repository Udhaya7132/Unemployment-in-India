#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\UDHAYA KUMAR . R\Desktop\Oasis\archive (2)\Unemployment_Rate_upto_11_2020.csv")


# In[3]:


df.head(3)


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.duplicated().sum()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df['Region.1'].value_counts()


# In[11]:


df['Region'].rename('State')


# In[12]:


df.columns


# In[13]:


df.rename(columns={'Region':'State'},inplace=True)


# In[14]:


df.columns


# In[16]:


df.columns = df.columns.str.strip()


# In[17]:


df['Date'] = pd.to_datetime(df['Date'])


# In[18]:


df['Date']


# In[19]:


df.head(3)


# In[20]:


df['Frequency'] = df['Frequency'].astype('category')


# In[21]:


df['Month'] = df['Date'].dt.month


# In[22]:


df.head(3)


# In[23]:


import calendar


# In[24]:


df['Month_int'] = df['Month'].apply(lambda x : int(x))
df['Month_name'] =  df['Month_int'].apply(lambda x: calendar.month_abbr[x])


# In[25]:


df.head(3)


# In[26]:


df.drop('Month',axis=1,inplace=True)


# In[27]:


df.shape


# In[28]:


df.rename(columns={'Region.1':'Region'},inplace=True)


# In[29]:


df.head(3)


# In[30]:


df.corr()


# In[31]:


round(df.describe(),2)


# In[32]:


df_groupby = round(df.groupby('Region')[['Estimated Unemployment Rate (%)', 'Estimated Employed','Estimated Labour Participation Rate (%)']].mean(),2)


# In[33]:


df_groupby.reset_index()


# In[34]:


x = df['Region']
y = df['Estimated Unemployment Rate (%)']


# In[35]:


plt.scatter(x,y)

plt.show()


# In[36]:


df.columns


# In[37]:


import pandas as pd
import plotly.express as px

a = df[['Estimated Unemployment Rate (%)', 'State']]
b = a.groupby('State').mean().reset_index()  

fig = px.bar(b, x='State', y='Estimated Unemployment Rate (%)', title='Average Unemployment Rate by State')

fig.show()


# In[38]:


import pandas as pd
import plotly.express as px

a = df[['Estimated Unemployment Rate (%)', 'State']]
b = a.groupby('State').mean().reset_index()  

b = b.sort_values(by='Estimated Unemployment Rate (%)',ascending=False)

fig = px.bar(b, x='State', y='Estimated Unemployment Rate (%)', title='Average Unemployment Rate by State')

fig.show()


# In[39]:


df.columns


# In[40]:


df[['Estimated Unemployment Rate (%)','Estimated Labour Participation Rate (%)']]


# In[41]:


import pandas as pd
import plotly.express as px

a = df[['Estimated Labour Participation Rate (%)', 'State']]
b = a.groupby('State').mean().reset_index()  

#b = b.sort_values(by='Estimated Labour Participation Rate (%)',ascending=False)

fig = px.bar(b, x='State', y='Estimated Labour Participation Rate (%)', title='Average Labour Participation Rate by State')


fig.show()


# In[42]:


sns.heatmap(df.corr(),annot=True)

plt.show()


# In[43]:


data = df[['Estimated Unemployment Rate (%)','Estimated Employed','Estimated Labour Participation Rate (%)','Region']]

fig = px.scatter_matrix(data,template='plotly',
    dimensions=['Estimated Unemployment Rate (%)','Estimated Employed','Estimated Labour Participation Rate (%)'],
                        color='Region')

fig.show()


# In[44]:


b = df.groupby('State')['Estimated Unemployment Rate (%)'].mean().reset_index()


b = b.sort_values(by='Estimated Unemployment Rate (%)', ascending=False)

plt.figure(figsize=(12, 6))
ax = sns.barplot(data=b, x='State', y='Estimated Unemployment Rate (%)', order=b['State'], palette='viridis')
plt.title('Average Unemployment Rate by State')
plt.xlabel('State')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.xticks(rotation=90)  
ax.legend(labels=['Average Unemployment Rate'], loc='upper right')

plt.tight_layout()
plt.show()


# In[45]:


d1 = df.groupby(['Month_name'])[['Estimated Unemployment Rate (%)','Estimated Labour Participation Rate (%)']].mean().reset_index()
d1


# In[46]:


month = d1.Month_name
month


# In[47]:


unemp_rate = d1['Estimated Unemployment Rate (%)']
unemp_rate


# In[48]:


labor_rate = d1['Estimated Labour Participation Rate (%)']
labor_rate


# In[49]:


import plotly.graph_objects as go
import plotly.express as px
fig = go.Figure()

fig.add_trace(go.Bar(x=month, y=unemp_rate, name="Unemployment Rate"))
fig.add_trace(go.Bar(x=month, y=labor_rate, name="Labour Participation Rate"))

fig.update_layout(title = "Unemploymnet Rate and Labour Participation rate ",
                 xaxis= {"categoryorder":"array","categoryarray":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]})
fig.show()


# In[50]:


fig = px.bar(df, x='Month_name', y='Estimated Employed', color='Month_name',
            #category_orders = {"Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]},
            title = 'Estimated employed people from Jan 2020 to Oct 2020')

fig.show()



# In[51]:


x = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
x


# In[52]:


regions = x.index
mean_unemployment_rates = x.values
colors = ('red','blue','green','orange')

plt.figure(figsize=(10, 6))
plt.bar(regions, mean_unemployment_rates, color=colors)
plt.xlabel('Region')
plt.ylabel('Mean Estimated Unemployment Rate (%)')
plt.title('Mean Estimated Unemployment Rate by Region')
plt.xticks(rotation=60)  
plt.show()


# In[53]:


df.columns


# In[54]:


fig = px.scatter_geo(df,'longitude', 'latitude', color="Region",
                     hover_name="State", size="Estimated Unemployment Rate (%)",
                     animation_frame="Month_name",scope='asia',template='seaborn',title='Impact of lockdown on Employement across regions')

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000

fig.update_geos(lataxis_range=[5,35], lonaxis_range=[65, 100],oceancolor="lightblue",
    showocean=True)

fig.show()


# In[55]:


before_pandemic = df[(df['Month_int']>=1) & (df['Month_int']<4)]
after_pandemic = df[(df['Month_int']>=4) & df['Month_int']<=7]


# In[56]:


bf_pandemic = before_pandemic.groupby('State')['Estimated Unemployment Rate (%)'].mean().reset_index()


# In[57]:


af_pandemic = after_pandemic.groupby('State')['Estimated Unemployment Rate (%)'].mean().reset_index()


# In[58]:


bf_pandemic['Unemployment Rate before Lockdown'] = af_pandemic['Estimated Unemployment Rate (%)']


# In[59]:


bf_pandemic.columns=['State','Unemployment Rate before Lockdown','Unemployment Rate after Lockdown']


# In[60]:


lockdown = df[(df['Month_int'] >= 4) & (df['Month_int'] <=7)]
before_lock = df[(df['Month_int'] >= 1) & (df['Month_int'] <=4)]

g_lockdown = lockdown.groupby('State')['Estimated Unemployment Rate (%)'].mean().reset_index()

g_bf_lock = before_lock.groupby('State')['Estimated Unemployment Rate (%)'].mean().reset_index()


g_lockdown['Unemployment Rate before lockdown'] = g_bf_lock['Estimated Unemployment Rate (%)']

g_lockdown.columns = ['State','Unemployment Rate after lockdown','Unemployment Rate before lockdown']

g_lockdown.head(2)


# In[61]:


g_lockdown['Percentage change in Unemployment'] = round(g_lockdown['Unemployment Rate after lockdown'] - g_lockdown['Unemployment Rate before lockdown']/g_lockdown['Unemployment Rate before lockdown'],2)

plot_per = g_lockdown.sort_values('Percentage change in Unemployment')

fig = px.bar(plot_per, x='State',y='Percentage change in Unemployment',color='Percentage change in Unemployment',
            title='Percentage change in Unemployment in each state after lockdown',template='ggplot2')

fig.show()

Most Affected / Impacted States During Pandemic 

Puducherry
Jharkhand
Bihar
Haryana
Tripura
# In[62]:


def sort_impact(x):
    if x <= 10:
        return 'Low Impact'
    elif x <= 20:
        return 'Moderate Impact'
    elif x <= 30:
        return 'High Impact'
    elif x <= 46:
        return 'Very High Impact'
    return 'Extreme Impact'


# In[68]:


plot_per['Impact Status'] = plot_per['Percentage change in Unemployment'].apply(lambda x: sort_impact(x))

fig = px.bar(plot_per, y='State', x='Percentage change in Unemployment', color='Impact Status',
             title='Impact of Lockdown on Employment Across States', template='ggplot2', height=650)

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




