# coding: utf-8

# graphing multiple days at once; be sure to update 'a' as needed
[sns.distplot(d1[x],hist=False,color=((y+0.5)/a,0.2,0.5,(y+0.5)/a), label=x, axlabel='YoY OpenTable Delta; Past '+str(a)+' Days' ) for y,x in enumerate(list(d1.columns)[-a:])]

# a bar chart of just today, by city - it makes a pretty rainbow
type(sns.barplot(d1[d].sort_values(), d1[d].sort_values().index ))

# simply just show the timeline of a city of statistic
sns.lineplot( d1.columns, d1.loc['Daily Median'] )
