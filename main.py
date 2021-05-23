import matplotlib.pyplot as plt

# Edit here
initialBalance = 1000  # starting amount of money
interestRate = 7  # in % per year
months = 96  # months to compute
monthlyContribution = 0  # monthly contribution to the balance

## Do not edit below ##
# Monthly interest rate
minterestRate = ((100+(interestRate))/100)**(1/12)

# y coordinates
list = [initialBalance]

# Compute all data
for i in range(months):
    list.append(list[i]*(minterestRate) + monthlyContribution)

# Plot
plt.plot(list)
plt.ylabel('Money')
plt.xlabel('Months')
plt.show()
