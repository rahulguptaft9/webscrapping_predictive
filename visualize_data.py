import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

sns.countplot(data=df, x='stock_text')
plt.title("Stock Availability (Books to Scrape)")
plt.xticks(rotation=15)

plt.savefig("stock_availability_plot.png")  # ✅ Save the plot
print("Chart saved as stock_availability_plot.png")
