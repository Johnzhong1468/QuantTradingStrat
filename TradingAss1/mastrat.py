"""    
ORIE 5230 Trading Assignment 1

Simple moving average crossover
From research, short MA: 2, long MA: 185
every day, long if SMA 2 is greater than SMA 185, short otherwise
"""

def initialize(context):
    set_benchmark(symbol('SPY'))
    # context.tic = sid(24) # AAPL
    context.tic = sid(5061) # MSFT
    
    #Run algo daily
    schedule_function(ma_crossover, 
                      date_rules.every_day())

def ma_crossover(context, data):
    hist = data.history( 
        context.tic,
        fields= 'price', 
        bar_count=200, 
        frequency='1d'
    )
 
    sma_long = hist[-185:].mean()
    sma_short = hist[-2:].mean()
 
# see all open orders.
    open_orders = get_open_orders()
 
# If no open orders, long all 
#execute scheduled market order if SMA short is greater than SMA long. 
    if sma_short > sma_long:
        if context.tic not in open_orders:
            order_target_percent(context.tic, 1.0)
   
# If no open orders, short all
#execute scheduled market order if SMA long is greater than SMA short. 
    elif sma_long > sma_short: 
        if context.tic not in open_orders:
            order_target_percent(context.tic, -1.0)