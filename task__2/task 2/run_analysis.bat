@echo off
REM CODE ALPHA INTERNSHIP - Books Data Analysis
REM Comprehensive Analysis + Power BI Preparation

echo.
echo ============================================================
echo CODE ALPHA INTERNSHIP - BOOKS DATA ANALYSIS
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and add to PATH
    pause
    exit /b 1
)

echo [1/2] Installing dependencies...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Done!

echo.
echo [2/2] Running analysis...
echo.
python code_alpha_analysis.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Analysis script failed
    pause
    exit /b 1
)

echo.
echo [3/3] Generating Power BI files...
echo (Skipped: CSV exports are generated inside code_alpha_analysis.py)


echo.
echo ============================================================
echo ✅ ANALYSIS COMPLETE!
echo ============================================================
echo.
echo Generated Files:
echo   - 8 Visualizations (PNG files @ 300 DPI)
echo   - 5 Power BI CSV exports
echo   - Power BI Setup Guides
echo.
echo Next Steps:
echo   1. Open 'powerbi_import_instructions.txt'
echo   2. Follow setup guide in Power BI Desktop
echo   3. Create dashboard from templates provided
echo.
echo For manual analysis, check:
echo   - powerbi_dashboard_guide.txt (Dashboard design)
echo   - powerbi_dax_measures.txt (DAX formulas)
echo.
pause
