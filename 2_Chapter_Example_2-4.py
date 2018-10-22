
# Example 2.4 Paying Off Bank Loan
# Bank loans are paid in equal installments.
# You have a loan of 1000 to be paid in 4 installments over 4 years.
# the rate is 10%

pv = 1000
r = 0.1
t = 4

# First you need to calculate the annuity factor. That is the number that multiplied by the pmt will give you the pv.

af = ((1/r)-(1/(r*(1+r)**t)))

# Then, in order to know the PMT, you divide the PV by the annuity factor

pmt = pv/af

print(pmt)


---

#  Example 2.4
# Table 2.1

import pandas as pd
import numpy as np
from datetime import date
pd.set_option('display.max_columns', 50)

# Basic facts from the loan

r = 0.1
years = 4
payments_year = 1
t = years*payments_year
pv = 1000
t_0 = date(2018,10,21)

# how much is the value of each payment (pmt)

pmt = np.pmt(r,t,pv)

# Now, how much of the pmt is interests (i) and how much is principal (p)?

# Period to calculate
per = 1

# Calculate the interest
ipmt = np.ipmt(r/payments_year, per, t, pv)

# Calculate the principal
ppmt = np.ppmt(r/payments_year, per, t, pv)

# Now, let us create a table for this data set.

# first we create the date range for all the payment periods

rng = pd.date_range(start=t_0,periods=t,freq='365D')
rng.name = "Date"


# Then, we create the columns for the table. We do that by creating a "Data Frame" in Pandas
# we use the date range as index.

df = pd.DataFrame(index=rng, columns=['Beg Balance','intermed','Interest', 'Total year end payment','Amortization of loan', 'End of year Balance'], dtype='float')
df.reset_index(inplace=True)
df.index += 1
df.index.name = "Year"


# now we populate the table with the values from the pmts

df["Total year end payment"] = np.pmt(r/payments_year, t, pv)
df["Amortization of loan"] = np.ppmt(r/payments_year, df.index, t, pv)
df["Interest"] = np.ipmt(r/payments_year, df.index, t, pv)
df["End of year Balance"] = (df["Amortization of loan"]).cumsum()
df["intermed"] = pv
df["Beg Balance"] = (df["End of year Balance"]+ df["intermed"])

# I am stuck. .....
# Whenever I try to calculate the value of the Beginning of year balance. I end up with a science notation number.
#  df["Beg Balance"] = (df["End of year Balance"]+ df["intermed"])
# Basically, it should calculate the pv - the value in the "End of Year Balance" column...

print(df)
