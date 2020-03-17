# coding: utf-8

%run import_data.py

plt.figure(figsize=(10,5))

a = 6
dd = d1[-a:].to_numpy().transpose()
ii = d1.columns
ll = d1[-a:].index.tolist()
wide_df = pd.DataFrame( dd, ii, ll )
ax = sns.lineplot(data=wide_df)

ax.set_xticklabels( ax.get_xticklabels(),rotation=45,horizontalalignment='right',fontweight='light',fontsize='x-large' )


ax.set_yticklabels( ax.get_yticklabels(),rotation=45,horizontalalignment='right',fontweight='light',fontsize='x-small' )
