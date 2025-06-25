# 📦 Stockout Predictor — Data Pipeline & AI-Powered Retail Insights

A hands-on data engineering and analytics project that scrapes live product availability from an e-commerce bookstore (BooksToScrape), stores it in a PostgreSQL database, processes it for insights, and uses machine learning and LLMs to predict and summarize stockout behavior.

---

## 🚀 Features

- 🔍 **Web Scraping**: Extracts book titles, prices, and stock status from multiple pages of an e-commerce demo site.
- 🛢️ **Database Integration**: Loads scraped data into a PostgreSQL table using SQLAlchemy.
- 🧼 **Data Cleaning**: Processes and engineers features such as binary stock indicators and price normalizations.
- 🤖 **Predictive Modeling**: Uses a Random Forest Classifier to predict stockout likelihood based on pricing.
- 📊 **Visualization**: Generates a count plot to visualize stock availability trends.
- 🧠 **AI-Powered Summarization**: Leverages OpenRouter GPT-4o to generate executive summaries of the dataset.

---

## 🧰 Tech Stack

- **Python** · `pandas`, `requests`, `BeautifulSoup`, `sqlalchemy`, `scikit-learn`, `matplotlib`, `seaborn`, `openai`
- **Database** · PostgreSQL
- **AI** · OpenRouter + GPT-4o (via `openai.ChatCompletion`)
- **Platform** · Ubuntu / WSL

---

## 📂 Project Structure

```
scrape_products.py        # Web scraping logic
load_to_postgres.py       # Loads CSV into PostgreSQL
clean_data.py             # Prepares and cleans the dataset
train_model.py            # Trains predictive model
summarize_data_ai.py      # Summarizes data using GPT-4o
visualize_data.py         # Visualizes stock distribution
```

---

## 📈 Sample Output

- `scraped_data.csv` — Raw scraped book data
- `cleaned_data.csv` — Processed dataset with engineered features
- `stock_availability_plot.png` — Bar chart of stock availability
- AI Summary — Human-readable summary of trends in the dataset

---

## 🔁 Usage

```bash
python3 scrape_products.py
python3 load_to_postgres.py
python3 clean_data.py
python3 train_model.py
python3 summarize_data_ai.py
python3 visualize_data.py
```

---

## 🎓 Ideal For

- Graduate-level research assistantships
- Demonstrating data pipeline and ML skills in interviews
- Showcasing LLM integration in business analytics workflows

---
