# coding: utf-8
import pandas as pd
import seaborn as sns
import matplotlib as plt
import sys
from scipy.stats import norm


a = 20
fl = 'opentable_314.xlsx'

d0 = pd.read_excel(fl)
d1 = d0.set_index('City')
d1.columns = pd.Series(d1.columns).apply(lambda x: x.strftime('%m-%d') if type(x) != str else x)
d1 = d1.drop('New Orleans')
d1 = d1.drop(('AVERAGE'))
d1 = d1.drop(('Ciudad de México'))
d1 = d1.drop(('London'))
d1 = d1.drop(('San Pedro Garza García'))
d1 = d1.drop('Hamburg')
d1 = d1.drop('München')
d1 = d1.drop('Dublin')
