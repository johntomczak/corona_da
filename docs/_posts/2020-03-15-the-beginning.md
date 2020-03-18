---
layout: post
title:  "Original Post"
date:   2020-03-15 20:42:00 -0500

---

I am not really sure where I came across this dataset. Like the rest of us, I have been consuming a lot of media this ~week. I think the link came up on Hacker News and an email newsletter and a few times on Twitter. Regardless, I finally clicked it, and was quickly taken in. Restaurants seatings seem like a fairly good proxy for social activity. Not sure that that presumption needs a lot of explanation.

To get a sense of it, I copy and pasted to an Excel file and overlaid some heat maps and other conditional formattings. I was first struck by the clear outliers - NYC, SF, and Seattle. They had massive (more than -20%) for many more days than the rest of the cities. This makes sense, at least as far at he news reports have been saying.

I was able to make a few observations here. First, the numbers out of New Orleans are funny looking. My friend Rem Houghton and I were just poking around the dataset in Excel, and saw that they had two +100% YoY deltas. Of course, that probably had to with Mardi Gras. You can download and review yourself, but we resolved that the changing dates of Lent, YoY, made it such that this year's dates would show massive growth, whereas last year's dates would set the bar too high for 2020 too. I decided to drop the New Orleans row because of this. Of course, other cities might have seen some pushes from Mardi Gras, but I am not going to get into that now.

Similarly, each city has their own unique fingerprint of social, or even professional conference, events. And then it should be noted that some of the one-off moves can be attributed to weather. One last thought - something could have happened in a city last year that significantly depressed dining out then, so this year's "jump" is in fact a return to normal habits. We don't get that granularity from OpenTable.

Then I got to the good stuff - loading into a (python) pandas dataframe. Once there, I was able to make some seaborn distplots and see some cool stuff.

I will just share one tonight: The past 10 nights. As the time stamp should say, I am writing this on Sunday night, so Saturday 3/14 (pi) is my latest night.

Each day's curve is set it up to get more opaque, and from blue to pink (keeping it simple), as we get closer to last night.

You can see that as time progresses the medians (peaks) come down and the spread widens. Also, it looks like there is a shift from up to Sunday and Monday onward. I am not sure what changed, but maybe it is because everyone got a little more worked up once they got back to chatting with colleagues (in person or online).

![My screenshot](assets/Last10Days_OpenTable.png)
