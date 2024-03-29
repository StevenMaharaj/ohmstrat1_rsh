import pandas as pd

df = pd.read_csv("./sym_table.csv")

assets = [
    "BTC",
    "ETH",
    "BNB",
    "ADA",
    "XRP",
    "DOGE",
    "DOT",
    "UNI",
    "LTC",
    "LINK",
    "BCH",
    "XLM",
    "FIL",
    "TRX",
    "EOS",
    "GALA",
    "SHIB",
    "SOL",
    "ICP",
    "CAKE",
    "DASH",
    "ETC",
    "VET",
    "XMR",
    "NEO",
    "MKR",
    "AAVE",
    "ATOM",
    "ALGO",
    "WAVES",
    "XTZ",
    "ZEC",
    "COMP",
    "YFI",
    "KSM",
    "ZIL",
    "OMG",
    "QTUM",
    "HOT",
    "SC",
    "ZEN",
    "LSK",
    "NANO",
    "ONT",
    "RVN",
    "BTT",
    "DGB",
    "STX",
    "LRC",
    "BNT",
    "MANA",
    "SUSHI",
    "CRV",
    "REN",
    "1INCH",
    "GRT",
    "ANKR",
    "SAND",
    "RLC",
    "BAND",
    "OCEAN",
    "MATIC",
    "SKL",
    "CELO",
    "ICX",
    "LUNA",
    "CHZ",
    "STMX",
    "CVC",
    "BTS",
    "DENT",
    "NMR",
    "RSR",
    "LPT",
    "BTT",
    "DGB",
    "STX",
    "LRC",
    "BNT",
    "MANA",
    "SUSHI",
    "CRV",
    "REN",
    "1INCH",
    "GRT",
    "ANKR",
    "SAND",
    "RLC",
    "BAND",
    "OCEAN",
    "MATIC",
    "SKL",
    "CELO",
    "ICX",
    "LUNA",
    "CHZ",
    "STMX",
    "CVC",
    "BTS",
    "DENT",
    "NMR",
    "RSR",
    "LPT",
]

symbols = map(lambda x: x + "_USDT", assets)

df = df[df["name"].isin(symbols)]
df.drop("Unnamed: 0", inplace=True, axis=1)
df.set_index("name", inplace=True)
df_filtered = df[df["value_usd"] < 1.0]

print(df_filtered)
