import openai
import pandas as pd
import os
# OpenRouter credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_type = "openai"
openai.api_version = None

df = pd.read_csv("cleaned_data.csv")
summary_text = df.head(20).to_string(index=False)

response = openai.ChatCompletion.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful data analyst."},
        {"role": "user", "content": f"Summarize this dataset for a business audience:\n\n{summary_text}"}
    ],
    temperature=0.6,
    max_tokens=1000 
)

print("AI Summary:")
print(response['choices'][0]['message']['content'])
