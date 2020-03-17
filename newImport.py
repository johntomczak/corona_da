# coding: utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import datetime
from scipy.stats import norm

# I label each day's download with the latest included evening
d = datetime.datetime.now() - datetime.timedelta(days=1)
d = d.strftime('%m_%d')

# as of now, I just keep the file in the same dir
fl = 'opentable_' + str(d) + '.xlsx'
d1 = pd.read_excel(fl)

d1 = d1[d1.columns[::-1]]
d1 = d1.set_index('Name')

# please blame my friend Rem if you go blind on this one - he is the King of One-Lining
d1.columns = pd.Series(d1.columns).apply(lambda x: x.strftime('%m_%d') if type(x) != str else x)

# NOLA has to go because of Mardi Gras moving around on the calendar
d1 = d1.drop('New Orleans')

# just want to stick to N. Am. cities, idk
d1 = d1.drop('London')
d1 = d1.drop('Hamburg')
d1 = d1.drop('München')
d1 = d1.drop('Dublin')

# don't need
# d1 = d1.drop( 'State', 1 )
# d1 = d1.drop( 'Country', 1 )

info = d1.describe()
# d1 = d1.append(info)
