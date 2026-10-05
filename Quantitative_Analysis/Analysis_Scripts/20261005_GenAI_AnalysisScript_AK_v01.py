"""
Generative AI Research - Survey Data Analysis Script
REIT6811 Applied Class 6

This script performs basic analysis on survey data collected for the
"Using Generative AI Tools - Boon or Bane" research project.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load survey data
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "Survey_Data", "20261005_GenAI_SurveyData_AK_v01.csv")
df = pd.read_csv(DATA_PATH)

# Basic statistics
print("=== Survey Data Summary ===")
print(f"Total participants: {len(df)}")
print(f"Average age: {df['Age'].mean():.1f}")
print(f"Average productivity rating: {df['Productivity_Rating(1-10)'].mean():.1f}")

# AI tool usage frequency
print("\n=== AI Tool Usage Frequency ===")
print(df['Frequency_of_Use'].value_counts())

# Productivity rating by tool
print("\n=== Average Productivity Rating by AI Tool ===")
print(df.groupby('AI_Tool_Used')['Productivity_Rating(1-10)'].mean())

# Recommendation rate
recommend_rate = (df['Recommend_AI'] == 'Yes').mean() * 100
print(f"\n=== Recommendation Rate: {recommend_rate:.1f}% ===")

# Generate a simple bar chart
plt.figure(figsize=(8, 5))
df.groupby('AI_Tool_Used')['Productivity_Rating(1-10)'].mean().plot(kind='bar', color='steelblue')
plt.title('Average Productivity Rating by AI Tool')
plt.xlabel('AI Tool')
plt.ylabel('Average Productivity Rating (1-10)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "..", "Analysis_Reports", "productivity_by_tool.png"))
print("\nChart saved to Analysis_Reports/productivity_by_tool.png")
