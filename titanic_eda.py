import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def analyze_titanic() -> None:
    sns.set_theme(style="whitegrid")
    titanic_df = sns.load_dataset("titanic")

    print("Titanic Dataset - First 5 Rows")
    print(titanic_df.head())
    print("\nDataset Info")
    print(titanic_df.info())
    print("\nMissing Values")
    print(titanic_df.isnull().sum())
    print("\nSummary Statistics")
    print(titanic_df.describe(include="all"))
    print("\nSurvival Rate by Sex")
    print(titanic_df.groupby("sex")["survived"].mean())
    print("\nSurvival Rate by Passenger Class")
    print(titanic_df.groupby("class")["survived"].mean())

    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(8, 5))
    sns.countplot(data=titanic_df, x="survived", hue="survived", palette="Set2", legend=False)
    plt.title("Passenger Survival Count")
    plt.xlabel("Survived (0 = No, 1 = Yes)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "survival_count.png"))
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(data=titanic_df, x="age", hue="survived", bins=30, kde=True, multiple="stack")
    plt.title("Age Distribution by Survival")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "age_distribution_by_survival.png"))
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=titanic_df, x="class", y="fare", hue="class", palette="pastel", legend=False)
    plt.title("Fare Distribution by Passenger Class")
    plt.xlabel("Passenger Class")
    plt.ylabel("Fare")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "fare_distribution_by_class.png"))
    plt.close()

    print(f"\nVisualization files saved in: {output_dir}")


if __name__ == "__main__":
    analyze_titanic()
