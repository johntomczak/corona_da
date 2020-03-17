# coding: utf-8
get_ipython().run_line_magic('run', 'import_data.py')
nums = d1[d][:-7].sort_values()
sns.barplot(nums, nums.index )
