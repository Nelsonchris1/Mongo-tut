from util import create_connection
import pandas as pd

def read_data():
    inventory = create_connection()
    results = inventory.find()
    invent = []
    for result in results:
        invent.append(result)
    inventory_df = pd.DataFrame(invent)
    return inventory_df

def write_data(df):
    return df.to_csv('inventory.csv')