import pandas
from constants import *


df = pandas.read_excel(EXCEL_PATH)


def save(star_list):
    saved_df = pandas.DataFrame(star_list, columns =[X_KEY, Y_KEY, COLOR_KEY])
    saved_df.to_excel(EXCEL_PATH, index=False)
