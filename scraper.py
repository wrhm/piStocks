from yahoo_finance import Share

f = open('portfolio.txt','r')
lines = [e[:-1].split() for e in f.readlines()]
purchase_date = lines[0][0]
shares = dict()
for [ticker,amt] in lines[1:]:
    shares[ticker] = int(amt)

purchase_prices = dict()
current_prices = dict()
for e in shares:
    eobj = Share(e)
    eobj.refresh()
    ehist = eobj.get_historical(purchase_date,purchase_date)
    purchase_prices[e] = (float) (ehist[0]['Open'])
    current_prices[e] = (float) (eobj.get_price())

print 'AT PURCHASE (%s):'%purchase_date
total_value_at_purchase = 0.0
for e in shares:
    #purchase price per share
    ppps = purchase_prices[e]
    value_at_purchase = shares[e] * ppps
    total_value_at_purchase += value_at_purchase
    print '%4s: %d @ $%.3f = $%.4f'%(e,shares[e],
            ppps,value_at_purchase)
print 'Total stock value: $%.4f'%total_value_at_purchase

today_date = Share('YHOO').get_trade_datetime()
print '\nAT PRESENT (%s):'%(today_date)
total_stock_value = 0.0
for e in shares:
    this_value = shares[e] * current_prices[e]
    total_stock_value += this_value
    print '%4s: %d @ $%.3f = $%.4f'%(e,shares[e],
            current_prices[e],this_value)
print 'Total stock value: $%.4f'%total_stock_value
