from yahoo_finance import Share

purchase_date = '2017-01-30'
shares = {'LSCC' : 1,
          'OSUR' : 1,
          'SID' : 2}

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

print ''

#today_date = Share('YHOO').get_trade_datetime().split()[0]
today_date = Share('YHOO').get_trade_datetime()
print 'AT PRESENT (%s):'%(today_date)
total_stock_value = 0.0
for e in shares:
    this_value = shares[e] * current_prices[e]
    total_stock_value += this_value
    print '%4s: %d @ $%.3f = $%.4f'%(e,shares[e],
            current_prices[e],this_value)
print 'Total stock value: $%.4f'%total_stock_value
