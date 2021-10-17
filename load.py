# importing necessary libraries
import psycopg2 as pg
import pandas as pd

# set output display size
pd.set_option("display.max_columns", None)

#connecting postgres database for fatching data
conn = pg.connect(database = "hospital", user = "postgres", password = "psql", host = "127.0.0.1", port = "5432")

#data load in pandas dataframe
df = pd.read_sql('select * from patients',con=conn)
# set customer ID as a index of dataframe
df.set_index(['customer_id'], inplace=True)
#printting data types of dataframe
print(df.dtypes)
#extracting specific Country data
ans = df[df['country'] == "IND"]
print(ans) # printing data

