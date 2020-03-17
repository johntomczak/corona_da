# coding: utf-8

%run import_data.py
plt.figure()
fri = sns.distplot( d1['03_13'] )
sat = sns.distplot( d1['03_14'] )
sun = sns.distplot( d1['03_15'] )
plt.legend( ['fri','sat','sun'] )
