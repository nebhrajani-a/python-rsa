import pandas as pd
from os import path

def save_table(usr_data):
    usr_data.to_pickle("usr_data.pkl")

def read_table():
    return pd.read_pickle("usr_data.pkl")
if not path.exists("usr_data.pkl"):
    usr_data = pd.DataFrame(columns = ['username', 'password', 'p', 'q', 'n', 'e', 'd', 'bits'])
    usr_data.loc[0] = ['root', '', 11, 3, 33, 3, 7, '1']
    save_table(usr_data)


def add_data(data):
    usr_data = read_table()
    usr_data.loc[usr_data.index.max() + 1, :] = data
    save_table(usr_data)

def search_column(column, value):
    usr_data = read_table()
    result = (usr_data[usr_data[column] == value])
    if result.empty:
        return False
    else:
        return True
def get_field(key, column):
    usr_data = read_table()
    x = usr_data.username[usr_data.username.str.contains('|'.join(key.split(' ')))]
    index = x.index[0]
    return usr_data.iloc[index][column]
def get_index(key, column):
    usr_data = read_table()
    x = usr_data.username[usr_data.username.str.contains('|'.join(key.split(' ')))]
    index = x.index[0]
    return index

def drop_row(key):
    usr_data = read_table()
    index = get_index(key, 'user')
    usr_data.drop([index], inplace = True)
