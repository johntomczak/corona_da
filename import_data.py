# coding: utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import datetime
from scipy.stats import norm

d = datetime.datetime.now() - datetime.timedelta(days=1)
d = d.strftime('%m_%d')
a = 10
fl = 'opentable_' + str(d) + '.xlsx'

d0 = pd.read_excel(fl)
d1 = d0.set_index('City')
d1.columns = pd.Series(d1.columns).apply(lambda x: x.strftime('%m_%d') if type(x) != str else x)
d1 = d1.drop('New Orleans')
d1 = d1.drop(('Ciudad de México'))
d1 = d1.drop(('London'))
d1 = d1.drop(('San Pedro Garza García'))
d1 = d1.drop('Hamburg')
d1 = d1.drop('München')
d1 = d1.drop('Dublin')

d1 = d1.drop( 'State', 1 )
d1 = d1.drop( 'Country', 1 )

# print( d1[d].sort_values(ascending=True).head(5) )
# maxD = pd.Series( ['NaN','NaN'], index=['State','Country'], name="Daily Max" )
# minD = pd.Series( ['NaN','NaN'], index=['State','Country'], name="Daily Min" )

info = d1.describe().drop('count')
d1 = d1.append(info)

# maxD = pd.Series( name="Daily Max" )
# minD = pd.Series( name="Daily Min" )
# medD = pd.Series( name="Daily Median" )
# stdD = pd.Series( name="Daily Std Dev" )
#
#
# for x in d1.columns:
#     # if x != 'State' and x != 'Country':
#     f = pd.Series( pd.Series( [max(d1[x])], index = [x], name="Daily Max" ) )
#     maxD = maxD.append( f )
#     f = pd.Series( pd.Series( [min(d1[x])], index = [x], name="Daily Min" ) )
#     minD = minD.append( f )
#     f = pd.Series( pd.Series( [np.median(d1[x])], index = [x], name="Daily Median" ) )
#     medD = medD.append( f )
#     f = pd.Series( pd.Series( [np.std(d1[x])], index = [x], name="Daily Std Dev" ) )
#     stdD = stdD.append( f )
#
# d1 = d1.append( minD )
# d1 = d1.append( maxD )
# d1 = d1.append( medD )
# d1 = d1.append( stdD )
