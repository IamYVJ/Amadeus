from Brokrage_Calculator import calculate_brokrage
from Clear_Screen import clear_Screen
import time
from Exit_Terminal import exit_Terminal

def print_dash():
    print("------------------------------------------------------------------------------------")

def start_print():
    print()
    print()
    print()
    print_dash()
    print()
    print("                          Brokrage Calculator")
    print("                              YVJ Systems")
    print()
    print_dash()
    print()
    print()
    print()

def print_head():
    print()
    print()
    print_dash()
    print()
    print("                          Brokrage Calculator")
    print("                              YVJ Systems")
    print()
    print_dash()
    print()

def quit_prg():
    clear_Screen()
    start_print()
    time.sleep(2)
    exit_Terminal()

def error_found(msg):
    print()
    print_dash()
    print()
    print("Error Occured")
    print("Error Message: " + msg)
    print()
    n = input("Enter Y To Restart Else Quit: ")
    if n.upper()=="Y":
        driver()
    else:
        quit_prg()
def driver():
    clear_Screen()
    start_print()
    time.sleep(2)
    clear_Screen()
    print_head()
    try:
        buy_price = input("Enter Buy Price: ")
        sell_price = input("Enter Sell Price: ")
        quantity = input("Enter Trade Quantity: ")
        if quantity.find(".")!=-1:
            error_found("Invalid Quantity")
        quantity = int(quantity)  
        print("1) Equity Delivery")
        print("2) Equity Intraday")
        print("3) Equity Futures")
        print("4) Equity Options")
        trade_type = input("Enter Trade Type (1/2/3/4): ")
        if trade_type=="1":
            trade_type = "Equity Delivery"
        elif trade_type=="2":
            trade_type = "Equity Intraday"
        elif trade_type=="3":
            trade_type = "Equity Futures"
        elif trade_type=="4":
            trade_type = "Equity Options"
        else:
            error_found("Invalid Trade Type")
        exchange = input("Enter Exchange (NSE/BSE): ")
        if exchange.upper()!="NSE" and exchange.upper()!="BSE":
            error_found("Invalid Exchange")
        if buy_price.find(".")!=-1:
            buy_price = buy_price[:buy_price.find(".")+2]
        buy_price = float(buy_price)
        if sell_price.find(".")!=-1:
            sell_price = sell_price[:sell_price.find(".")+2]
        sell_price = float(sell_price)
        
        net = calculate_brokrage(buy_price, sell_price, quantity, trade_type, exchange)
        net = str(net)
        print()
        if net.find(".")!=-1:
            net = net[:net.find(".")+2]
        print("Net PnL: " + str(net))
        print()
        print_dash()
        print()
        n = input("Enter Y To Restart Else Quit: ")
        if n.upper()=="Y":
            driver()
        else:
            quit_prg()
    except Exception as e:
        error_found(str(e))

driver()
