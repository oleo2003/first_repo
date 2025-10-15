import pandas as pd
import matplotlib.pyplot as plt
file_path = "Mantamonis_bacterial_contamination_analysis.xlsx"
df = pd.read_excel(file_path)
print("Columns:", df.columns.tolist())
if "Preliminary Verdict:" in df.columns:
    counts = df["Preliminary Verdict:"].value_counts()
    plt.figure(figsize=(8, 6))
    counts.plot(kind='bar', color='skyblue')
    plt.title("Preliminary Verdict Classifications")
    plt.xlabel("Court")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("preliminary_classification.png")
    print("Saved: preliminary_classification.png")
else:
    print("Column 'preliminary verdicts' not found. Please check the Excel column name.")
