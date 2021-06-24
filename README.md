# Repository to keep track of MBS-related calculation/prove-out scripts

calculateFactor ->
  takes input from user for original balance and current balance and returns the factor.
  
calculateAccruedInterest ->
  takes input from user for original face amt, fact, price, coupon, and settlement day (in format of the numerical day of the month).
  returns a nicely formatted ticket including original face, current factor, current face, principal value, accrued number of days + gross interest, and the total accrued interest amount.
