import pandas as pd

usr_data = pd.DataFrame(columns = ['username', 'password', 'p', 'q', 'n', 'e', 'd'])

usr_data.loc[0] = ['root', '', 11, 3, 33, 3, 7]


def add_data(data):
    usr_data.loc[usr_data.index.max() + 1, :] = data

def search_column(column, value):
    result = (usr_data[usr_data[column] == value])
    if result.empty:
        return False
    else:
        return True

datax = ['wavion', 'wavion', 3, 5, 15, 5, 0]
add_data(datax)

# print(search_column('username', 'Aditya'))

# print(usr_data)
