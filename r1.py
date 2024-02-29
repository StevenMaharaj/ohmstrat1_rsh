import pandas as pd




df = pd.read_csv('./sym_table.csv')

assets = ["GALA","CAKE","SHIB","DASH","BNB","ICP"]

symbols = map(lambda x: x + "_USDT", assets)


df = df[df['name'].isin(symbols)]


print(df)
