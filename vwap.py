# ['ProductionYear', 'VolIGWh', 'Price', 'TradeDate', 'CY', 'TradeYear', 'TradeMon', 'VolTimesPrice', 'DummyDate']


def myvwap(TY, TM, PY, data):
    subset = data[(data['TradeYear']==TY) & (data['TradeMon']==TM) & (data['ProductionYear']==PY)]
    sumProd = subset['VolTimesPrice'].sum()
    # print('Sumprod', sumProd)
    sumVol = subset['VolIGWh'].sum()
    # print('Sumvol', sumVol)
    if sumVol!=0:
        averagePrice = sumProd/sumVol
    else:
        # give zero price if no trades
        averagePrice = 0
    # print('VWAP', averagePrice)
    return averagePrice


def myvol(TY, TM, PY, data):
    subset = data[(data['TradeYear']==TY) & (data['TradeMon']==TM) & (data['ProductionYear']==PY)]
    sumVol = subset['VolIGWh'].sum()
    return sumVol