import pandas as pd

df = pd.read_csv('./sym_table.csv')

assets = ["BTC","ETH","BNB","ADA","XRP",
          "DOGE","DOT","UNI","LTC","LINK",
          "BCH","XLM","FIL","TRX","EOS",
          "GALA","SHIB","SOL","ICP","CAKE",
          "DASH"]

symbols = map(lambda x: x + "_USDT", assets)
    
df = df[df['name'].isin(symbols)]
df.drop("Unnamed: 0",inplace=True,axis=1)
df.set_index("name",inplace=True)
df_filtered = df[df['value_usd'] < 1.0]

print(df_filtered)
