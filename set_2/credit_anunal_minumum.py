def monthlyCalculation (bal, inter, pay):
  unpaid = bal - pay
  return {
      'remain': unpaid + unpaid*inter/12.0,
      'pay_min': pay
      }

def annualCalculation(bal, inter, pay):
  remaining = bal
  totalPaid = 0
  for i in range(12):
    monthly = monthlyCalculation(remaining, interest, pay)
    remaining = monthly['remain']
    totalPaid += monthly['pay_min']
  return{'remain': remaining, 'paid': totalPaid}

def calculateBound(bal, monthlyInterestRate):
  return{
      'lower': bal/12,
      'upper': (bal*((1 + monthlyInterestRate)**12))/12.0
      }

balance = int(raw_input("balance:"))
interest = float(raw_input("interest rate:"))
monthlyInterestRate = interest/12.0
bound = calculateBound(balance, monthlyInterestRate)
monthlyLowerBound = bound['lower']
monthlyUpperBound = bound['upper']
#payment = float(raw_input("payment rate:"))

monthlyPaid = (monthlyLowerBound + monthlyUpperBound)/2
pay = 0
remain = balance

while abs(remain) > 0.01:
  annual = annualCalculation(balance, interest, monthlyPaid)
  pay = annual['paid']
  remain = annual['remain']

  if remain < 0:
    monthlyUpperBound = monthlyPaid
  else:
    monthlyLowerBound = monthlyPaid
  #monthlyPaid += 10
  monthlyPaid = (monthlyLowerBound + monthlyUpperBound)/2

print('Lowest Payment: ' + str(round(monthlyPaid, 2)))
