from newImport import load
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# ----------
# yes, i am going to make a notes section of code snippets, lol
# ----------
# fl = 'docs/assets/'+str(t0)+'_recent_three.png'
# recent_three.savefig(fl)
# ----------

# ----------
# dates of the last three days
# ----------
t0 = datetime.datetime.now() - datetime.timedelta(days=1)
t0 = t0.strftime('%m_%d')
t1 = datetime.datetime.now() - datetime.timedelta(days=2)
t1 = t1.strftime('%m_%d')
t2 = datetime.datetime.now() - datetime.timedelta(days=3)
t2 = t2.strftime('%m_%d')

# ----------
# the actual importing
# ----------
d1 = load()
info = d1.describe()

# ----------
# last three days plot
# ----------
recent_three=plt.subplot(2,1,1)
plt.style.use('classic')
fri = sns.distplot( d1[t0] )
sat = sns.distplot( d1[t1] )
sun = sns.distplot( d1[t2] )
plt.legend( [str(t0), str(t1), str(t2)] )

# ----------
# ----------
# today=plt.figure()
today=plt.subplot(2,1,2)
dist_today = sns.distplot( d1[t0], bins=20 )
# fl = 'docs/assets/'+str(d)+'_dist_today.png'
# dist_today.savefig(fl)

# ----------
# ----------
bars=plt.figure()
sorted_cities = sns.barplot(d1[t0].sort_values(), d1[t0].sort_values().index )
# fl = 'docs/assets/'+str(d)+'_sorted_cities.png'
# sorted_cities.savefig(fl)

# ----------
# ----------
print( d1[t0].sort_values() )
print( "shutdown " + str( sum( d1[t0]==-1) ) )
print( d1[t0].describe() )

plt.show()
