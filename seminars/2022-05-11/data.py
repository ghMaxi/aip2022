import pandas
from constants import PATH, WHITE

df = pandas.read_excel(PATH, index_col=0)


def save():
    df.to_excel(PATH)


def append(phase, x, y):
    global df
    new_df = pandas.DataFrame({'id': [-1], 'phase': [phase], 'full_time': [60], 'x': [x], 'y': [y]})
    df = pandas.concat([df, new_df], axis=0)




if __name__ == "__main__":
    print(df)
