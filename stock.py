from yahoo_finance import Share

def getData(ticker):
  yahoo = Share( ticker )
  print "___________"
  print "___________"
  print ticker;
  print "___________"
  print "Price:" , yahoo.get_price(), yahoo.get_change();
  print "PE:", yahoo.get_price_earnings_ratio()
  print "Yield:", yahoo.get_dividend_yield()
  print "Market Cap:", yahoo.get_market_cap()
  print "Year-High:", yahoo.get_year_high()
  print "Year-Low:" , yahoo.get_year_low()
  print "50day mov Avg:" , yahoo.get_50day_moving_avg();
  print "200day mov Avg:" , yahoo.get_200day_moving_avg();
  print "Volume:" , yahoo.get_volume() , ", Avg Vol: ", yahoo.get_avg_daily_volume() ;
  return;

#print ticker;
#getData( ticker) ;
getData( 'AAPL' ) ;
getData( 'AMD' ) ;
getData( 'BIIB' ) ;
getData( 'BMY' ) ;
getData( 'BRKB' ) ;
getData( 'FXE' ) ;
getData( 'FXY' ) ;
getData( 'GILD' ) ;
getData( 'GLD' ) ;
getData( 'GOOG' ) ;
getData( 'INFY' ) ;
getData( 'JPM' ) ;
getData( 'MA' ) ;
getData( 'MAPIX' ) ;
getData( 'MINDX' ) ;
getData( 'MRK' ) ;
getData( 'MSFT' ) ;
getData( 'NVDA' ) ;
getData( 'QCOM' ) ;
getData( 'PCI' ) ;
getData( 'REGN' ) ;
getData( 'V' ) ;
getData( 'VMW' ) ;
getData( 'WFC' ) ;
getData( 'Y' ) ;
