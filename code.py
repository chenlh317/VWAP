import numpy as np, pandas as pd, os
# import my functions
import vwap

# read file. Only allows ONE product in each file!

# Make sure the titles are
# ['ProductionYear', 'VolIGWh', 'Price', 'TradeDate', 'CY', 'TradeYear', 'TradeMon', 'VolTimesPrice', 'DummyDate']
# only these are used: ProductionYear, VolIGWh, Price, TradeYear, TradeMon, VolTimesPrice
# make sure the titles' name

# from pandas import DataFrame

# may need to change file name if processing other products
trades = pd.read_csv("Nordic.hydro.trades.csv")

# test, true val = 8.66, 1540
# print(vwap.myvwap(2015,4,2015,trades), vwap.myvol(2015,4,2015,trades),)

# give months
monthsRaw = pd.date_range(start='20110401', periods=100, freq='1M')
months = []

# convert timestamp to a string
for item in monthsRaw:
    months.append(item.strftime('%Y-%m-%d'))

# prod year series
ProdYearSer = np.linspace(2010, 2030, 21, dtype=int)

# tables for results
vwapTabel = pd.DataFrame(index=months, columns=ProdYearSer)
volTabel = pd.DataFrame(index=months, columns=ProdYearSer)

for thisMonth in months:
    for thisProdYr in ProdYearSer:
        # def myvwap(TY, TM, PY, data):
        # print(int(thisMonth[0:4]), int(thisMonth[5:7]), thisProdYr)
        # compute VWAP, round to 2 decimals
        thisVwap = vwap.myvwap(int(thisMonth[0:4]), int(thisMonth[5:7]), thisProdYr, trades)
        vwapTabel.ix[thisMonth, thisProdYr] = round(thisVwap, 2)
        # compute volume in GWh, round to 2 decimalsh
        thisVol = vwap.myvol(int(thisMonth[0:4]), int(thisMonth[5:7]), thisProdYr, trades)
        volTabel.ix[thisMonth, thisProdYr] = round(thisVol, 2)


print(vwapTabel)
print(volTabel)

print('Calculation completed!')
print('\n')

# give file name by product name
myFileName = input("Product name (e.g. Nordic hydro) = ")
print('\n')

# write to CSV
vwapTabel.to_csv('VWAP_' + myFileName + '.csv')
volTabel.to_csv('Volume_in_GWh_' + myFileName + '.csv')

# open directory
print('CSV files are ready. Check the folder!')
print('\n')
os.startfile(os.getcwd())


# plot heat map

# NOT working yet. Attempt to plot "Months" and get error!

# import seaborn as sns
# import matplotlib.pyplot as plt
#
#
# print(subVWAP)
# myHeat = sns.heatmap(subVWAP, annot=True, linewidths=.1)
#
# myHeat.xticks(np.arange(7) + 0.5, ProdYearSer)
# myHeat.yticks(np.arange(5) + 0.5, months)
#
# myHeat.set_title('VWAP of ' + myFileName)
# myHeat.set_xlabel('Production Year')
# myHeat.set_ylabel('')
#
# plt.show()