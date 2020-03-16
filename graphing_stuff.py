# coding: utf-8
[sns.distplot(d1[x],hist=False,color=((y+0.5)/a,0.2,0.5,(y+0.5)/a), label=x, axlabel='YoY OpenTable Delta; Past '+str(a)+' Days' ) for y,x in enumerate(list(d1.columns)[-a:])]
sns.lineplot( d1.columns, d1.loc['Minneapolis'] )
