import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')
#
# start = dt.datetime(2010,1,1)
# end = dt.datetime(2018,6,5)
# df = web.DataReader('TSLA', 'quandl',start,end)
# df.to_csv("tesla.csv")
# # print(df.head(10))
#
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)
# df['AdjClose'].plot()
# plt.show()

df['100ma'] = df['AdjClose'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index,df['AdjClose'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])
plt.show()
print (df.head)
