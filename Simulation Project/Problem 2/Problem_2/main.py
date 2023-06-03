from numpy import random
import matplotlib.pyplot as mp

# Variables used to store
Runs = 10
Sales = []
Overflow = []
Salvage = []
Profit = []
ProfitOfEachCase = []
optimalAns = 0
optimalProfit = 0

# Function to create Random numbers

def RandomProbability():
    Probability = random.uniform()
    return Probability

for j in range(200):
    TotalProfit = 0
    for i in range(Runs):
        Newspaper = 70
        Prob = RandomProbability()
        if Prob <= 0.18:
            NewsdayType = "Excellent"
            Prob = RandomProbability()
            if Prob <= 0.07:
                Demand = 50
            elif Prob <= 0.15:
                Demand = 60
            elif Prob <= 0.27:
                Demand = 70
            elif Prob <= 0.4:
                Demand = 80
            elif Prob <= 0.62:
                Demand = 90
            elif Prob <= 0.85:
                Demand = 100
            elif Prob <= 0.93:
                Demand = 110
            elif Prob <= 1:
                Demand = 120

            if Newspaper < Demand:
                Sales.append(Newspaper)
                Overflow.append(Demand - Newspaper)
                Salvage.append(0)
            elif Newspaper == Demand:
                Sales.append(Newspaper)
                Salvage.append(0)
                Overflow.append(0)
            elif Newspaper > Demand:
                Sales.append(Demand)
                Salvage.append(Newspaper - Demand)
                Overflow.append(0)

        elif Prob <= 0.6:
            NewsdayType = "Good"
            Prob = RandomProbability()
            if Prob <= 0.06:
                Demand = 40
            elif Prob <= 0.15:
                Demand = 50
            elif Prob <= 0.31:
                Demand = 60
            elif Prob <= 0.5:
                Demand = 70
            elif Prob <= 0.78:
                Demand = 80
            elif Prob <= 0.9:
                Demand = 90
            elif Prob <= 0.97:
                Demand = 100
            elif Prob <= 1:
                Demand = 110

            if Newspaper < Demand:
                Sales.append(Newspaper)
                Overflow.append(Demand - Newspaper)
                Salvage.append(0)
            elif Newspaper == Demand:
                Sales.append(Newspaper)
                Salvage.append(0)
                Overflow.append(0)
            elif Newspaper > Demand:
                Sales.append(Demand)
                Salvage.append(Newspaper - Demand)
                Overflow.append(0)

        elif Prob <= 0.92:
            NewsdayType = "Fair"
            Prob = RandomProbability()
            if Prob <= 0.15:
                Demand = 40
            elif Prob <= 0.37:
                Demand = 50
            elif Prob <= 0.65:
                Demand = 60
            elif Prob <= 0.83:
                Demand = 70
            elif Prob <= 0.93:
                Demand = 80
            elif Prob <= 0.98:
                Demand = 90
            elif Prob <= 1:
                Demand = 100

            if Newspaper < Demand:
                Sales.append(Newspaper)
                Overflow.append(Demand - Newspaper)
                Salvage.append(0)
            elif Newspaper == Demand:
                Sales.append(Newspaper)
                Salvage.append(0)
                Overflow.append(0)
            elif Newspaper > Demand:
                Sales.append(Demand)
                Salvage.append(Newspaper - Demand)
                Overflow.append(0)

        elif Prob <= 1:
            NewsdayType = "Poor"
            Prob = RandomProbability()
            if Prob <= 0.42:
                Demand = 40
            elif Prob <= 0.7:
                Demand = 50
            elif Prob <= 0.84:
                Demand = 60
            elif Prob <= 0.94:
                Demand = 70
            elif Prob <= 0.99:
                Demand = 80
            elif Prob <= 1:
                Demand = 90

            if Newspaper < Demand:
                Sales.append(Newspaper)
                Overflow.append((Demand - Newspaper))
                Salvage.append(0)
            elif Newspaper == Demand:
                Sales.append(Newspaper)
                Salvage.append(0)
                Overflow.append(0)
            elif Newspaper > Demand:
                Sales.append(Demand)
                Salvage.append((Newspaper - Demand))
                Overflow.append(0)
        #print(Sales)
        #print(Overflow)
        #print(Salvage)
        Revenue = ((70 * Sales[i + Runs*j]) - (50 * Newspaper) - (17 * Overflow[i + Runs*j]) + (15 * Salvage[i + Runs*j]))
        #print(Revenue)
        Profit.append(Revenue/100)
        #print(Profit)
        TotalProfit += Profit[i + Runs*j]
        #print(TotalProfit)

    #if TotalProfit > optimalProfit:
     #   optimalAns = 40 + 20*j
      #  optimalProfit = TotalProfit

    ProfitOfEachCase.append(TotalProfit)

fig, plot = mp.subplots()
plot.hist(ProfitOfEachCase)

plot.set_xlabel('Profit')
plot.set_ylabel('Occurence')
mp.show()

print('Optimal Number of Newspaper to buy is:' , optimalAns)
print('With average profit of:' , optimalProfit)