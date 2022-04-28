import pandas as pd
PATH = "../../df.csv"

df = None
if __name__ == "__main__":
    url = 'https://github.com/chris1610/pbpython/blob/master/data/2018_Sales_Total_v2.xlsx?raw=True'
    df = pd.read_excel(url)
    df.to_csv(PATH)
else:
    df = pd.read_csv(PATH)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
