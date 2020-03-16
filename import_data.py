# coding: utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import sys
import datetime
from scipy.stats import norm

d = datetime.datetime.now() - datetime.timedelta(days=1)
d = d.strftime('%m_%d')
a = 20
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

print( d1[d].sort_values(ascending=True).head(5) )
