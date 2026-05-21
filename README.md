# codealpha-task2-eda

Exploratory Data Analysis on Titanic dataset with visualization and insights.

## Requirements

- Python 3.8+
- pandas
- seaborn
- matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Titanic EDA

```bash
python titanic_eda.py
```

This script:

- Loads the Titanic dataset using Seaborn
- Prints dataset overview and summary statistics
- Performs basic survival analysis
- Saves visualizations to `outputs/`:
  - `survival_count.png`
  - `age_distribution_by_survival.png`
  - `fare_distribution_by_class.png`
