# Chapter 2
# Page 29
# Example 2.3 "Winning Big at the Lottery"

# $365 million was won in the lottery.
# It is  paid in 30 equal annual # installments of $12.167 Million each.
# Assuming that the first payment occurred at the end of one year,
# what was the present value of the prize?
# Note: the Interest rate at the time was 6%

# The payment constitute a 30-year annuity. We have to multiply the $12.167 million
# by the annuity factor:

pmt = 12167000
r = 0.06
t = 30

pv = pmt * ((1/r)-(1/(r*(1+r)**t)))

print(ceil(pv))

# Annuity due
# is when the annuity pays the first pmt at t = 0. 
# for calculating the PV of the Annuity due, the formula is slightly different. 
# basically we have to calculate PV * (1+r)
# An annuity due is worth (1+r) times the PV of the normal Annuity
# pv_annuity_due = pv*(1+r)
