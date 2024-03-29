import pandas as pd




df = pd.read_csv('./sym_table.csv')

# assets = ["GALA","CAKE","SHIB","DASH","BNB","ICP"]
assets = ["BTC","ETH","BNB","ADA","XRP","DOGE","DOT","UNI","LTC","LINK","BCH","XLM","FIL","TRX","EOS"]

symbols = map(lambda x: x + "_USDT", assets)


df = df[df['name'].isin(symbols)]


# print(df)

df_filtered = df[df['value_usd'] < 1.0]
print(df_filtered)
