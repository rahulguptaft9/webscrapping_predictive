import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:mypassword@localhost:5432/stockout_db")
#engine = create_engine("postgresql://postgres@localhost:5432/stockout_db")
df = pd.read_csv("scraped_data.csv")
df.to_sql("product_availability", con=engine, if_exists="replace", index=False)
