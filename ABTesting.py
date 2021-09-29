
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
df_control.head()

df_test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")
df_test.head()

### Defination of Hypothesis for A/B Testing

#H0: There is no statistically significant difference between the average earnings values of the Control group with the "Maximum Bidding" campaign and the Test group with the "Average Bidding" campaign.
#H1: There is a statistically significant difference between the average of the earnings values of the Control group with the "Maximum Bidding" campaign and the Test group with the "Average Bidding" campaign.

### Assumptions Control

#### Normallity Assumption

##### -H0: The assumption of normal distribution is provided.
##### -H1: The assumption of normal distribution is not provided.

##### -If p-value < 0.05 then H0 reject.
##### -If p-value is not <0.05 then H0 can not be rejected.

#####Normality Assumption Test by Shapiro Algorithm

test_stat, pvalue = shapiro(df_control["Earning"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df_test["Earning"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#####According to the result of p values, HO can not be rejected.


###Variance Homogeneity Assumption


##### H0: Variences have homogeneity.
##### H1: Variences have not homogeneity.

###### p-value < ise 0.05 'ten HO RED.
###### p-value < değilse 0.05 H0 REDDEDILEMEZ.

###### Variance Homogeneity Assumption Test by Levene Algorithm

test_stat, pvalue = levene(df_control["Earning"],
                            df_test["Earning"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##### According to the result of p-values H0 can not be rejected.

#### Independent Two-Sample T-Test applied as assumptions are provided.


test_stat, pvalue = ttest_ind(df_control["Earning"],
                              df_test["Earning"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##### RESULT : H0 rejected. There is a statistically significant difference between the mean earnings of the Test and Control groups with 95% confidence.


df_control["Earning"].mean()
df_test["Earning"].mean()


##### It has been determined that there is a statistical difference between "Maximum Bidding" and "Average Bidding" in terms of "Earning". When we look at the average earnings values, it can be said that it is more profitable to switch to the "Average Bidding" method, as there is a higher return on earnings.