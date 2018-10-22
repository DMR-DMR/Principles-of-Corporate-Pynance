# Chapter 2
# Page 28
# Example 2.2
# Cost of an installment plan
# You get offered to buy a new Toyota for $5K a year paid at the end of each year for a period of 5 years. With no upfront payment. How much does the Toyota really cost to you?.

# pv = ?

r = 0.07
pmt = 5000
t = 5

# This is an annuity. Because consists of regular payments for a fixed period of time.

pv = pmt * ((1/r)-(1/(r*(1+r)**t)))

print(pv)
