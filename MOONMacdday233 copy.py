import pyupbit
import talib
import time
import telegram

token = "5276186721:AAHXzlWxhysToV7v5AKFa3DRVlu1NCU9syo"
bot = telegram.Bot(token)
chat_id = -1001295886155

ticker = "KRW-ETH"
interval = "days"
fastperiod=2
slowperiod=3
signalperiod=3


while True:
    try:
        df = pyupbit.get_ohlcv(ticker, interval=interval)
        macd, macdsignal, macdhist = talib.MACD(df['close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
        print(macd[-1],macdsignal[-1])
        if macd[-1] > macdsignal[-1]:
            while True:
                try:
                    df = pyupbit.get_ohlcv(ticker, interval=interval)
                    macd, macdsignal, macdhist = talib.MACD(df['close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
                    print(macd[-1],macdsignal[-1])
                    if macd[-1] < macdsignal[-1]:                        
                        bot.sendMessage(chat_id=chat_id, text="데드 크로스 포착 240분 Macd")
                        while True:
                            try:
                                df = pyupbit.get_ohlcv(ticker, interval=interval)
                                macd, macdsignal, macdhist = talib.MACD(df['close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
                                print(macd[-1],macdsignal[-1])                                
                                if macd[-1] > macdsignal[-1]:                                    
                                    bot.sendMessage(chat_id=chat_id, text="골든 크로스 포착 240분 Macd")
                                    y = 0
                                    break
                                time.sleep(1)
                            except Exception as e:
                                print(e)
                                time.sleep(1)
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    time.sleep(1)        
        time.sleep(1)        
    except Exception as e:
        print(e)
        time.sleep(1)    
            
