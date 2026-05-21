CODE ALPHA INTERNSHIP — Books Data Analysis (Task 2)

This folder contains the end-to-end analysis pipeline for the books dataset.

1) Files
- code_alpha_analysis.py
  Main script that:
  • Loads powerbi_books_detailed.csv
  • Prints dataset overview + KPIs
  • Generates visualizations (PNG, 300 DPI)
  • Exports Power BI-ready summary CSVs

- eda.py
  Additional EDA script (generates eda_analysis.png) and runs statistical checks.

- run_analysis.bat
  One-click launcher.

2) How to run
Windows:
- Double-click: run_analysis.bat

Manual:
- From this folder:
  py code_alpha_analysis.py
  py eda.py

3) Outputs
Visualizations (PNG @ 300 DPI):
- 01_price_distribution.png
- 02_rating_distribution.png
- 03_price_by_category.png
- 04_rating_by_category.png
- 05_price_vs_rating.png
- 06_availability_status.png
- 07_category_distribution.png
- 08_heatmap_rating_analysis.png

EDA output:
- eda_analysis.png

Power BI exports (CSV):
- powerbi_category_summary.csv
- powerbi_rating_summary.csv
- powerbi_availability_summary.csv
- powerbi_kpi_summary.csv

4) Notes
If your system doesn’t recognize the `python` command, use the `py` launcher (e.g. `py code_alpha_analysis.py`).

