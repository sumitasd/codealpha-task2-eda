"""
Exploratory Data Analysis (EDA) - Books Dataset
================================================
This script performs comprehensive exploratory data analysis including:
- Data structure and type exploration
- Trend and pattern identification
- Anomaly detection
- Statistical hypothesis testing
- Data quality assessment
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# SECTION 1: LOAD AND INITIAL EXPLORATION
# ============================================================================

print("=" * 80)
print("EXPLORATORY DATA ANALYSIS - BOOKS DATASET")
print("=" * 80)

# Load dataset
# Prefer dataset that exists in this task folder (recommended for this repo)
dataset_path = Path(__file__).parent / "powerbi_books_detailed.csv"
if not dataset_path.exists():
    # Fallback to legacy path if present
    legacy_path = Path(__file__).parent.parent / "New folder" / "books_dataset.csv"
    dataset_path = legacy_path

df = pd.read_csv(dataset_path)


print("\n[SECTION 1] INITIAL DATA OVERVIEW")
print("-" * 80)
print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nFirst Few Records:")
print(df.head(10))

# ============================================================================
# SECTION 2: DATA STRUCTURE & TYPES
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 2] DATA STRUCTURE & TYPES")
print("-" * 80)

print("\nData Types & Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe(include='all'))

# ============================================================================
# SECTION 3: MEANINGFUL QUESTIONS & EXPLORATION
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 3] ASKING MEANINGFUL QUESTIONS")
print("-" * 80)

questions = [
    "Q1: What is the price distribution of books?",
    "Q2: What are the most common book ratings?",
    "Q3: How many unique values exist in each column?",
    "Q4: What percentage of data is missing (null)?",
    "Q5: What is the relationship between price and rating?",
    "Q6: Are there price outliers in the dataset?",
    "Q7: What is the stock availability status?",
    "Q8: Are there any data type inconsistencies?"
]

for q in questions:
    print(f"\n{q}")

# ============================================================================
# SECTION 4: DATA QUALITY ASSESSMENT
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 4] DATA QUALITY & ISSUES")
print("-" * 80)

print(f"\n✓ Missing Values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': missing.index,
    'Missing_Count': missing.values,
    'Missing_Percentage': missing_pct.values
})
print(missing_df.to_string(index=False))

print(f"\n✓ Duplicate Records:")
duplicates = df.duplicated().sum()
print(f"  Total duplicate rows: {duplicates}")
if duplicates > 0:
    print(f"  Duplicate titles: {df[df.duplicated(subset=['Title'], keep=False)].shape[0]}")

print(f"\n✓ Unique Values per Column:")
for col in df.columns:
    unique_count = df[col].nunique()
    print(f"  {col}: {unique_count} unique values")

# ============================================================================
# SECTION 5: PRICE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 5] PRICE ANALYSIS")
print("-" * 80)

# Convert price to numeric (remove £ symbol)
df['Price_Numeric'] = df['Price'].str.replace('£', '').astype(float)

print(f"\nPrice Statistics:")
print(f"  Mean Price: £{df['Price_Numeric'].mean():.2f}")
print(f"  Median Price: £{df['Price_Numeric'].median():.2f}")
print(f"  Std Dev: £{df['Price_Numeric'].std():.2f}")
print(f"  Min Price: £{df['Price_Numeric'].min():.2f}")
print(f"  Max Price: £{df['Price_Numeric'].max():.2f}")
print(f"  Q1 (25%): £{df['Price_Numeric'].quantile(0.25):.2f}")
print(f"  Q3 (75%): £{df['Price_Numeric'].quantile(0.75):.2f}")

# Identify outliers using IQR method
Q1 = df['Price_Numeric'].quantile(0.25)
Q3 = df['Price_Numeric'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Price_Numeric'] < Q1 - 1.5 * IQR) | (df['Price_Numeric'] > Q3 + 1.5 * IQR)]

print(f"\n⚠ Price Outliers (IQR method):")
print(f"  Number of outliers: {len(outliers)}")
if len(outliers) > 0:
    print(f"  Outlier range: > £{Q3 + 1.5 * IQR:.2f} or < £{Q1 - 1.5 * IQR:.2f}")
    print(f"  Example outliers:")
    print(outliers[['Title', 'Price', 'Rating']].head())

# ============================================================================
# SECTION 6: RATING ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 6] RATING ANALYSIS")
print("-" * 80)

rating_order = ['One', 'Two', 'Three', 'Four', 'Five']
rating_mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Numeric'] = df['Rating'].map(rating_mapping)

print(f"\nRating Distribution:")
rating_counts = df['Rating'].value_counts().reindex(rating_order)
rating_pct = (rating_counts / len(df)) * 100

for rating in rating_order:
    count = rating_counts.get(rating, 0)
    pct = rating_pct.get(rating, 0)
    print(f"  {rating:8s}: {int(count):3d} books ({pct:5.1f}%)")

print(f"\nRating Statistics:")
print(f"  Mean Rating: {df['Rating_Numeric'].mean():.2f}")
print(f"  Median Rating: {df['Rating_Numeric'].median():.2f}")
print(f"  Mode Rating: {df['Rating_Numeric'].mode().values[0]}")

# ============================================================================
# SECTION 7: CORRELATION & RELATIONSHIPS
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 7] PRICE vs RATING RELATIONSHIP")
print("-" * 80)

# Correlation analysis
correlation = df['Price_Numeric'].corr(df['Rating_Numeric'])
print(f"\nPearson Correlation (Price vs Rating): {correlation:.4f}")

print(f"\nAverage Price by Rating:")
price_by_rating = df.groupby('Rating', observed=True)['Price_Numeric'].agg([
    ('Count', 'count'),
    ('Mean Price', 'mean'),
    ('Median Price', 'median'),
    ('Std Dev', 'std')
]).reindex(rating_order)
print(price_by_rating)

# ============================================================================
# SECTION 8: ANOMALIES & DATA ISSUES
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 8] ANOMALIES & DATA ISSUES DETECTED")
print("-" * 80)

issues = []

# Issue 1: Empty Stock column (optional)
if 'Stock' in df.columns:
    if df['Stock'].isnull().all():
        issues.append("❌ Stock column is completely empty (no data)")
else:
    issues.append("ℹ 'Stock' column not present in dataset")


# Issue 2: All availability is same
if df['Availability'].nunique() == 1:
    issues.append(f"⚠ All products have same availability status: '{df['Availability'].iloc[0]}'")

# Issue 3: Price format consistency
if df['Price'].str.startswith('£').all():
    issues.append("✓ Price format is consistent (all have £ symbol)")

# Issue 4: Rating as text instead of numeric
if df['Rating'].dtype == 'object':
    if df['Rating'].isin(rating_order).all():
        issues.append("ℹ Rating stored as text (One/Two/Three/Four/Five) instead of numeric")
    else:
        issues.append("❌ Rating contains unexpected values")

# Issue 5: High variance in titles (potential data quality)
title_lengths = df['Title'].str.len()
if title_lengths.std() > title_lengths.mean() * 0.5:
    issues.append("ℹ Large variation in book title lengths")

# Issue 6: Price range analysis
price_range = df['Price_Numeric'].max() - df['Price_Numeric'].min()
if price_range > df['Price_Numeric'].mean() * 2:
    issues.append(f"ℹ Wide price range (£{df['Price_Numeric'].min():.2f} to £{df['Price_Numeric'].max():.2f})")

print("\nIdentified Issues:")
for issue in issues:
    print(f"  {issue}")

# ============================================================================
# SECTION 9: STATISTICAL HYPOTHESIS TESTING
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 9] HYPOTHESIS TESTING")
print("-" * 80)

from scipy import stats

# H0: Price is normally distributed
print("\nH1: Is price normally distributed?")
stat, pvalue = stats.shapiro(df['Price_Numeric'].dropna())
print(f"  Shapiro-Wilk Test: p-value = {pvalue:.6f}")
if pvalue < 0.05:
    print(f"  Result: REJECT null hypothesis - Price is NOT normally distributed")
else:
    print(f"  Result: FAIL TO REJECT - Price appears normally distributed")

# H0: Mean price is equal across rating groups
print("\nH2: Is mean price equal across all rating groups?")
groups = [df[df['Rating'] == rating]['Price_Numeric'].values for rating in rating_order if (df['Rating'] == rating).any()]
f_stat, pvalue = stats.f_oneway(*groups)
print(f"  One-way ANOVA: F-statistic = {f_stat:.4f}, p-value = {pvalue:.6f}")
if pvalue < 0.05:
    print(f"  Result: REJECT null hypothesis - Ratings affect price significantly")
else:
    print(f"  Result: FAIL TO REJECT - No significant price difference across ratings")

# ============================================================================
# SECTION 10: VISUALIZATIONS
# ============================================================================

print("\n" + "=" * 80)
print("[SECTION 10] GENERATING VISUALIZATIONS")
print("-" * 80)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Books Dataset - Exploratory Data Analysis', fontsize=16, fontweight='bold')

# 1. Price Distribution
axes[0, 0].hist(df['Price_Numeric'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].axvline(df['Price_Numeric'].mean(), color='red', linestyle='--', label=f'Mean: £{df["Price_Numeric"].mean():.2f}')
axes[0, 0].axvline(df['Price_Numeric'].median(), color='green', linestyle='--', label=f'Median: £{df["Price_Numeric"].median():.2f}')
axes[0, 0].set_xlabel('Price (£)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Price Distribution')
axes[0, 0].legend()

# 2. Rating Distribution
rating_counts_sorted = df['Rating'].value_counts().reindex(rating_order)
axes[0, 1].bar(rating_order, rating_counts_sorted.values, color='coral', alpha=0.7, edgecolor='black')
axes[0, 1].set_xlabel('Rating')
axes[0, 1].set_ylabel('Count')
axes[0, 1].set_title('Rating Distribution')
axes[0, 1].grid(axis='y', alpha=0.3)

# 3. Box plot for outliers
axes[0, 2].boxplot(df['Price_Numeric'], vert=True)
axes[0, 2].set_ylabel('Price (£)')
axes[0, 2].set_title('Price Box Plot (Outlier Detection)')
axes[0, 2].grid(axis='y', alpha=0.3)

# 4. Price vs Rating Scatter
for rating in rating_order:
    rating_data = df[df['Rating'] == rating]
    rating_num = rating_mapping[rating]
    axes[1, 0].scatter([rating_num] * len(rating_data), rating_data['Price_Numeric'], 
                       alpha=0.6, s=50, label=rating)
axes[1, 0].set_xlabel('Rating')
axes[1, 0].set_ylabel('Price (£)')
axes[1, 0].set_title('Price vs Rating Relationship')
axes[1, 0].set_xticks([1, 2, 3, 4, 5])
axes[1, 0].set_xticklabels(rating_order)
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

# 5. Average Price by Rating
price_by_rating_mean = df.groupby('Rating')['Price_Numeric'].mean().reindex(rating_order)
axes[1, 1].bar(rating_order, price_by_rating_mean.values, color='lightgreen', alpha=0.7, edgecolor='black')
axes[1, 1].set_xlabel('Rating')
axes[1, 1].set_ylabel('Average Price (£)')
axes[1, 1].set_title('Average Price by Rating')
axes[1, 1].grid(axis='y', alpha=0.3)

# 6. Data Completeness
completeness = (1 - df.isnull().sum() / len(df)) * 100
axes[1, 2].barh(df.columns, completeness.values, color='plum', alpha=0.7, edgecolor='black')
axes[1, 2].set_xlabel('Completeness (%)')
axes[1, 2].set_title('Data Completeness by Column')
axes[1, 2].set_xlim([0, 105])
for i, v in enumerate(completeness.values):
    axes[1, 2].text(v + 1, i, f'{v:.1f}%', va='center', fontsize=9)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'eda_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'eda_analysis.png'")
plt.close()

# ============================================================================
# SUMMARY REPORT
# ============================================================================

print("\n" + "=" * 80)
print("[SUMMARY REPORT]")
print("=" * 80)

summary = f"""
KEY FINDINGS:

1. DATASET OVERVIEW:
   - Total Records: {len(df)}
   - Total Columns: {len(df.columns)}
   - Data Quality: {'Poor' if len(issues) > 2 else 'Moderate' if len(issues) > 0 else 'Good'}

2. PRICE INSIGHTS:
   - Average Price: £{df['Price_Numeric'].mean():.2f}
   - Price Range: £{df['Price_Numeric'].min():.2f} - £{df['Price_Numeric'].max():.2f}
   - Distribution: {'Skewed' if abs(stats.skew(df['Price_Numeric'])) > 0.5 else 'Relatively Normal'}
   - Outliers Detected: {len(outliers)} ({(len(outliers)/len(df)*100):.1f}%)

3. RATING INSIGHTS:
   - Most Common Rating: {df['Rating'].mode().values[0]}
   - Rating Mean: {df['Rating_Numeric'].mean():.2f}/5.0
   - Overall Sentiment: {'Positive (avg > 3.5)' if df['Rating_Numeric'].mean() > 3.5 else 'Mixed'}

4. CORRELATION:
   - Price-Rating Correlation: {correlation:.4f} {'(weak/no relationship)' if abs(correlation) < 0.3 else '(moderate relationship)' if abs(correlation) < 0.7 else '(strong relationship)'}

5. DATA QUALITY ISSUES:
   - Total Issues Found: {len(issues)}
   - Critical Issues: {sum(1 for i in issues if '❌' in i)}
   - Main Problem: Stock column completely empty

6. RECOMMENDATIONS:
   - Fill or remove the empty Stock column
   - Validate that all records represent actual book inventory
   - Consider converting Rating to numeric format for analysis
   - Investigate any outlier-priced books for data entry errors
   - Verify price currency consistency (all are in pounds)
"""

print(summary)

print("=" * 80)
print("EDA ANALYSIS COMPLETE")
print("=" * 80)
