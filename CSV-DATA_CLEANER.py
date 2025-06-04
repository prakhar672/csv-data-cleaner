import pandas as pd

# Step 1: Load the CSV file
try:
    df = pd.read_csv('sample_data.csv')
    print("✅ CSV loaded successfully!")
except FileNotFoundError:
    print("❌ sample_data.csv not found. Make sure it's in the same folder.")
    exit()

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Fill missing values (NaN) with placeholder or 0
df = df.fillna("Unknown")  # or use 0 for numeric columns

# Step 4: Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("🎉 Cleaned CSV saved as 'cleaned_data.csv'")