---
layout: post
title:  "Big Monday"
date:   2020-03-15 22:30:00 -0500

---

First, allow me to introduce today's updated 10 Day Chart:
![March06-March15](/assets/315-10d.png)

It goes without saying that last night - Sunday night -  March 15 - Beware the Ides - was yet another major shift.

Here is March 15 just by itself, w a histograph (20 bins, range = -100% : 0%):

![March 15 histograph](/assets/315_precise_2.png)

---

Isn't this a pretty way of looking at all of today's reports?
![pretty](/assets/315_pretty.png)

```python
# d1 is the imported / cleaned import_data
# the last seven rows are stats
nums = d1[today][:-7].sort_values()


sns.barplot(nums, nums.index )
```

Check out the sorted numbers:
* **Top 5**
* San Francisco     -0.72
* Boston            -0.70
* New York          -0.69
* Seattle           -0.62
* Los Angeles       -0.57

Other than Los Angeles, I think (thru my personal media followings) that these are first cities you think of when you think of "coronavirus." I have not gotten to crossing the OpenTable data with the testing reports, but I think one can be satisfied for now.

* **Bottom 5**
* Charlotte         -0.36
* Minneapolis       -0.33
* Honolulu          -0.32
* Miami Beach       -0.23
* Tampa             -0.20

Being March, it is Spring Break season. No matter how you judge those participating now, there certainly have been mixed messages on the severity of this outbreak and one's personal responsibilities in fighting it.

So, I think seeing Miami Beach and Tampa and probably Honolulu (though maybe they are just so remote?) at the bottom seems sensible.

TO BE CLEAR, -20% YoY drops are still a shock to businesses and still reflect pretty solid, in an absolute sense, effects.

---

Finally, here is a look at the summary statistics for the whole dataset.

I have not yet thought about or dug into it much yet, as of writing.
![stats](/assets/315_daily_stats.png)
