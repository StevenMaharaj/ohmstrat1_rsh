import pandas as pd



def main():
    print("Reading CSV file")
    df = pd.read_csv('gioex.csv')
    df = df[["name","quanto_multiplier","mark_price","order_size_min"]]
    df["value_usd"] = df["mark_price"] * df["quanto_multiplier"] * df["order_size_min"]
    df = df.sort_values(by="value_usd")
    df.to_csv("sym_table.csv")
    print(df.head(15))

    # df_final = df.head(15)




if __name__ == "__main__":
    main()
