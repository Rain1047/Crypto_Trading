from libraries import *

df = pd.DataFrame([[1,2,3,4]])
print(df)

engine = create_engine(database_cp)
df = pd.read_sql('ticker_list',con=engine)
print(df)

class strategies():
    def __init__(self):
        pass

    def st_downtrend(self):
        pass
