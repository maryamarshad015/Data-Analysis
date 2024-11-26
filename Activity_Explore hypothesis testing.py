#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore hypothesis testing

# ## Introduction

# You work for an environmental think tank called Repair Our Air (ROA). ROA is formulating policy recommendations to improve the air quality in America, using the Environmental Protection Agency's Air Quality Index (AQI) to guide their decision making. An AQI value close to 0 signals "little to no" public health concern, while higher values are associated with increased risk to public health. 
# 
# They've tasked you with leveraging AQI data to help them prioritize their strategy for improving air quality in America.

# ROA is considering the following decisions. For each, construct a hypothesis test and an accompanying visualization, using your results of that test to make a recommendation:
# 
# 1. ROA is considering a metropolitan-focused approach. Within California, they want to know if the mean AQI in Los Angeles County is statistically different from the rest of California.
# 2. With limited resources, ROA has to choose between New York and Ohio for their next regional office. Does New York have a lower AQI than Ohio?
# 3. A new policy will affect those states with a mean AQI of 10 or greater. Will Michigan be affected by this new policy?
# 
# **Notes:**
# 1. For your analysis, you'll default to a 5% level of significance.
# 2. Throughout the lab, for two-sample t-tests, use Welch's t-test (i.e., setting the `equal_var` parameter to `False` in `scipy.stats.ttest_ind()`). This will account for the possibly unequal variances between the two groups in the comparison.

# ## Step 1: Imports
# 
# To proceed with your analysis, import `pandas` and `numpy`. To conduct your hypothesis testing, import `stats` from `scipy`.

# #### Import Packages

# In[1]:


# Import relevant packages

### YOUR CODE HERE ###
import pandas as pd
import numpy as np
from scipy import stats


# You are also provided with a dataset with national Air Quality Index (AQI) measurements by state over time for this analysis. `Pandas` was used to import the file `c4_epa_air_quality.csv` as a dataframe named `aqi`. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 
# **Note:** For purposes of your analysis, you can assume this data is randomly sampled from a larger population.

# #### Load Dataset

# In[2]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE ###
aqi = pd.read_csv('c4_epa_air_quality.csv')


# ## Step 2: Data Exploration

# ### Before proceeding to your deliverables, explore your datasets.
# 
# Use the following space to surface descriptive statistics about your data. In particular, explore whether you believe the research questions you were given are readily answerable with this data.

# In[3]:


# Explore your dataframe `aqi` here:

### YOUR CODE HERE ###
aqi.head(5)


# In[4]:


aqi.describe()


# In[5]:


aqi.info()


# In[6]:


aqi['local_site_name'].isnull().sum()


# In[8]:


aqi.dropna(subset=['local_site_name'],inplace=True)


# In[9]:


aqi['local_site_name'].isnull().sum()


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referring to the material on descriptive statisics.
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   Consider using `pandas` or `numpy` to explore the `aqi` dataframe.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
# Any of the following functions may be useful:
# - `pandas`: `describe()`,`value_counts()`,`shape()`, `head()`
# - `numpy`: `unique()`,`mean()`
#     
# </details>

# #### **Question 1: From the preceding data exploration, what do you recognize?**

# 3 rows for local_site_name were missing so i dropped those rows.

# 

# ## Step 3. Statistical Tests
# 
# Before you proceed, recall the following steps for conducting hypothesis testing:
# 
# 1. Formulate the null hypothesis and the alternative hypothesis.<br>
# 2. Set the significance level.<br>
# 3. Determine the appropriate test procedure.<br>
# 4. Compute the p-value.<br>
# 5. Draw your conclusion.

# ### Hypothesis 1: ROA is considering a metropolitan-focused approach. Within California, they want to know if the mean AQI in Los Angeles County is statistically different from the rest of California.
# 
# Before proceeding with your analysis, it will be helpful to subset the data for your comparison.

# In[10]:


aqi['state_name'].unique()


# In[11]:


aqi['county_name'].unique()


# In[23]:


# Create dataframes for each sample being compared in your test

### YOUR CODE HERE ###
df_cal_state = aqi[(aqi['state_name'] == 'California')  & (aqi['county_name'] != 'Los Angeles')]
df_la_county = aqi[aqi['county_name'] == 'Los Angeles']


# In[24]:


print(df_cal_state['aqi'].mean())
print(df_la_county['aqi'].mean())


# In[25]:


print(df_la_county['aqi'].mean() - df_cal_state['aqi'].mean())


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the material on subsetting dataframes.  
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   Consider creating two dataframes, one for Los Angeles, and one for all other California observations.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
# For your first dataframe, filter to `county_name` of `Los Angeles`. For your second dataframe, filter to `state_name` of `Calfornia` and `county_name` not equal to `Los Angeles`.
#     
# </details>

# #### Formulate your hypothesis:

# **Formulate your null and alternative hypotheses:**
# 
# *   $H_0$: There is no difference in the mean AQI between Los Angeles County and the rest of California.
# *   $H_A$: There is a difference in the mean AQI between Los Angeles County and the rest of California.
# 

# #### Set the significance level:

# In[26]:


# For this analysis, the significance level is 5%

### YOUR CODE HERE
significance_lvl = 0.05


# #### Determine the appropriate test procedure:

# Here, you are comparing the sample means between two independent samples. Therefore, you will utilize a **two-sample  𝑡-test**.

# #### Compute the P-value

# In[29]:


# Compute your p-value here

### YOUR CODE HERE ###
stats.ttest_ind(a = df_la_county['aqi'] , b =df_cal_state['aqi'], equal_var = False)


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the material on how to perform a two-sample t-test.
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   In `ttest_ind()`, a is the aqi column from our "Los Angeles" dataframe, and b is the aqi column from the "Other California" dataframe.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
#   Be sure to set `equal_var` = False.
# 
# </details>

# #### **Question 2. What is your P-value for hypothesis 1, and what does this indicate for your null hypothesis?**

# P-value = 0.04 or 4.9% < significance level 0.5 or 5% hence resulting in rejecting the null hypothesis.
# Hence the difference in the mean aqi rates between Los Angeles and the state California other than LA is due to significant reason and not due to a random chance.

# ### Hypothesis 2: With limited resources, ROA has to choose between New York and Ohio for their next regional office. Does New York have a lower AQI than Ohio?
# 
# Before proceeding with your analysis, it will be helpful to subset the data for your comparison.

# In[30]:


# Create dataframes for each sample being compared in your test

### YOUR CODE HERE ###
df_ny = aqi[aqi['state_name'] == 'New York']
df_ohio = aqi[aqi['state_name'] == 'Ohio']


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the materials on subsetting dataframes.  
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   Consider creating two dataframes, one for New York, and one for Ohio observations.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
# For your first dataframe, filter to `state_name` of `New York`. For your second dataframe, filter to `state_name` of `Ohio`.
#     
# </details>

# #### Formulate your hypothesis:

# **Formulate your null and alternative hypotheses:**
# 
# *   $H_0$: The mean AQI of New York is greater than or equal to that of Ohio.
# *   $H_A$: The mean AQI of New York is **below** that of Ohio.
# 

# #### Significance Level (remains at 5%)

# #### Determine the appropriate test procedure:

# Here, you are comparing the sample means between two independent samples in one direction. Therefore, you will utilize a **two-sample  𝑡-test**.

# In[31]:


df_ny['aqi'].mean() < df_ohio['aqi'].mean()


# #### Compute the P-value

# In[35]:


# Compute your p-value here

### YOUR CODE HERE ###
stats.ttest_ind(a = df_ny['aqi'] , b = df_ohio['aqi'],alternative = 'less', equal_var = False)
#as alternative hypothesis states mean aqi of NY is LESS than that Ohio 
#took the parameter alternative = 'less'


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the material on how to perform a two-sample t-test.
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   In `ttest_ind()`, a is the aqi column from the "New York" dataframe, an b is the aqi column from the "Ohio" dataframe.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
#   You can assign `tstat`, `pvalue` to the output of `ttest_ind`. Be sure to include `alternative = less` as part of your code.  
# 
# </details>

# #### **Question 3. What is your P-value for hypothesis 2, and what does this indicate for your null hypothesis?**

# The p-value is 0.03 < significance level 0.05 hence reject the null hypothesis and this infers the the mean aqi level for new york is less than that of Ohio.

# ###  Hypothesis 3: A new policy will affect those states with a mean AQI of 10 or greater. Will Michigan be affected by this new policy?
# 
# Before proceeding with your analysis, it will be helpful to subset the data for your comparison.

# In[36]:


# Create dataframes for each sample being compared in your test

### YOUR CODE HERE ###
df_michi = aqi[aqi['state_name'] == 'Michigan']


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the material on subsetting dataframes.  
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   Consider creating one dataframe which only includes Michigan.
# </details>

# #### Formulate your hypothesis:

# **Formulate your null and alternative hypotheses here:**
# 
# *   $H_0$: The mean AQI of Michigan is less than or equal to 10.
# *   $H_A$: The mean AQI of Michigan is greater than 10.
# 

# #### Significance Level (remains at 5%)

# #### Determine the appropriate test procedure:

# Here, you are comparing one sample mean relative to a particular value in one direction. Therefore, you will utilize a **one-sample  𝑡-test**. 

# #### Compute the P-value

# In[39]:


# Compute your p-value here

### YOUR CODE HERE ###
#as alternative hypo is having  a word greater so using the parameter alternative = 'greater' 

tstat, p_value = stats.ttest_1samp(df_michi['aqi'], 10, alternative = 'greater')
print(tstat)
print(p_value)


# <details>
#   <summary><h4><strong>HINT 1</strong></h4></summary>
# 
#   Consider referencing the material on how to perform a one-sample t-test.
# </details>

# <details>
#   <summary><h4><strong>HINT 2</strong></h4></summary>
# 
#   In `ttest_1samp)`, you are comparing the aqi column from your Michigan data relative to 10, the new policy threshold.
# </details>

# <details>
#   <summary><h4><strong>HINT 3</strong></h4></summary>
# 
#   You can assign `tstat`, `pvalue` to the output of `ttest_1samp`. Be sure to include `alternative = greater` as part of your code.  
# 
# </details>

# #### **Question 4. What is your P-value for hypothesis 3, and what does this indicate for your null hypothesis?**

# P-value = 0.9 is greater than significance-level = 0.05 hence failed to reject the null hypothesis meaning that mean aqi for michigan is less than or equal to 10 and this infers that Michigan will not be affected by the new policy.

# ## Step 4. Results and Evaluation
# 
# Now that you've completed your statistical tests, you can consider your hypotheses and the results you gathered.

# #### **Question 5. Did your results show that the AQI in Los Angeles County was statistically different from the rest of California?**

# Yes the results were statistically different and not due to random chance.

# #### **Question 6. Did New York or Ohio have a lower AQI?**

# NewYork have a lower mean aqi rate as comapred to that of Ohio.

# #### **Question 7: Will Michigan be affected by the new policy impacting states with a mean AQI of 10 or greater?**
# 
# 

# No Michigan will not be effected by the new government policy beacuse it has mean aqi less than or equal to 10.

# # Conclusion
# 
# **What are key takeaways from this lab?**
# 
# **What would you consider presenting to your manager as part of your findings?**
# 
# **What would you convey to external stakeholders?**
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
