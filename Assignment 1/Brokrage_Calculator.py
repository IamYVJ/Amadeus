def calculate_brokrage(buy_price, sell_price, quantity, trade_type, exchange):
    if trade_type=="Equity Delivery":
        brokerage = 0
        TT = 0.001*quantity*(buy_price+sell_price) #STT/CTT
        if exchange=="NSE":
            transaction_charges = 0.0000325*quantity*(buy_price+sell_price)
        else:
            transaction_charges = 0.00003*quantity*(buy_price+sell_price)
        stamp_duty = 0.0001*quantity*(buy_price+sell_price)
    elif trade_type=="Equity Intraday":
        brokerage = 0.0001*quantity*(buy_price+sell_price)
        if brokerage>40:
            brokerage = 40
        TT = 0.00025*quantity*(sell_price) #STT/CTT
        if exchange=="NSE":
            transaction_charges = 0.0000325*quantity*(buy_price+sell_price)
        else:
            transaction_charges = 0.00003*quantity*(buy_price+sell_price)
        stamp_duty = 0.00002*quantity*(buy_price+sell_price)
    elif trade_type=="Equity Futures":
        brokerage = 0.0001*quantity*(buy_price+sell_price)
        if brokerage>40:
            brokerage = 40
        TT = 0.01*quantity*(sell_price) #STT/CTT
        if exchange=="NSE":
            transaction_charges = 0.000019*quantity*(buy_price+sell_price)
        else:
            transaction_charges = 0.000019*quantity*(buy_price+sell_price)
        stamp_duty = 0.00002*quantity*(buy_price+sell_price)
    elif trade_type=="Equity Options":
        brokerage = 40
        TT = 0.0005*quantity*(sell_price) #STT/CTT
        if exchange=="NSE":
            transaction_charges = 0.0005*quantity*(buy_price+sell_price)
        else:
            transaction_charges = 0.0005*quantity*(buy_price+sell_price)
        stamp_duty = 0.00002*quantity*(buy_price+sell_price)
    GST = 0.18*(transaction_charges)
    SEBI = 10*((quantity*(buy_price+sell_price))/10000000)
    net = quantity*(sell_price-buy_price) - brokerage - TT - transaction_charges - GST - SEBI - stamp_duty

    return net

