"""
rename_notebooks.py
=====================

This utility script renames Jupyter notebooks in a specified directory
according to a predefined mapping.  It preserves the original file extension
(e.g. `.ipynb`) and only renames files that actually exist.

Usage:

    python rename_notebooks.py /path/to/ipynp

Replace `/path/to/ipynp` with the path containing your notebooks.  The
directory can be a Windows path (e.g. `C:\\Users\\UseR\\Desktop\\...`) or
a POSIX path (`/home/user/...`); Python will handle both.  If a file
listed in the mapping is not found, the script will report that it was
skipped.

Note: You should review and adjust the mapping below if your file names
differ or include extensions.  The keys (old names) should match your
current notebook filenames without extensions.  The values (new names)
represent the desired base name; the script appends the existing extension.
"""

import os
import sys
from pathlib import Path


def main(directory: str) -> None:
    # Define mapping from original base names (without extension)
    # to new base names (also without extension).  When renaming,
    # the script will preserve the existing file extension.
    rename_map = {
        "02.Python Tips #Numpy와 Pandas": "STEP02_Python-Tips-Numpy-and-Pandas",
        "02.Python Tips #Pandas Indexing": "STEP02_Python-Tips-Pandas-Indexing",
        "02.고객별 연간 지출액 예측 (Linear Regression)": "STEP02_Annual-Spending-Prediction-Linear-Regression",
        "03. 광고 반응률 예측 (Logistic Regression)": "STEP03_Ad-Response-Prediction-Logistic-Regression",
        "03.Python Tips #Unique, Value Counts": "STEP03_Python-Tips-Unique-Value-Counts",
        "04. Python Tips # List": "STEP04_Python-Tips-List",
        "04. Python Tips #For, While": "STEP04_Python-Tips-For-While",
        "04. 고객 이탈 예측 (KNN)": "STEP04_Customer-Churn-Prediction-KNN",
        "05. 구매 요인 분석 (Decision Tree)": "STEP05_Purchase-Factor-Analysis-Decision-Tree",
        "06. 프로모션 효율 예측 (Random Forest)": "STEP06_Promotion-Efficiency-Prediction-Random-Forest",
        "07. 고객 분류 (KMeans) - Part 1": "STEP07_Customer-Clustering-KMeans-Part1",
        "07. 고객 분류 (KMeans) - Part 2": "STEP07_Customer-Clustering-KMeans-Part2",
        "08. 쇼핑몰 매출 예측 (Time Series) - Part 1": "STEP08_Sales-Prediction-Time-Series-Part1",
        "08. 쇼핑몰 매출 예측 (Time Series) - Part 2": "STEP08_Sales-Prediction-Time-Series-Part2",
        "09. 상품 리뷰 분석(NLP) - Part 1": "STEP09_Product-Review-Analysis-NLP-Part1",
        "09. 상품 리뷰 분석(NLP) - Part 2": "STEP09_Product-Review-Analysis-NLP-Part2",
        "10. GA 데이터 적용 시나리오 - Part 1": "STEP10_GA-Data-Application-Scenario-Part1",
        "10. GA 데이터 적용 시나리오 - Part 2": "STEP10_GA-Data-Application-Scenario-Part2",
        "11. 데이터 시각화 (Visualization)": "STEP11_Data-Visualization",
        "Python Tips # Data Merge (concat, merge, join)": "Python-Tips-Data-Merge-Concat-Merge-Join",
        "Python Tips # groupby _ set_index": "Python-Tips-Groupby-Set-Index",
        "Python Tips # 함수 만들기(Def)": "Python-Tips-Function-Def",
        "Python Tips # 함수 만들기(if)": "Python-Tips-Function-If",
        "단축키": "Shortcuts",
    }

    base_path = Path(directory).expanduser().resolve()
    if not base_path.exists() or not base_path.is_dir():
        print(f"Error: '{base_path}' is not a valid directory.")
        return

    print(f"Scanning directory: {base_path}")

    # Iterate through the mapping and attempt to rename files
    for old_base, new_base in rename_map.items():
        # Look for files with any extension
        matched_files = list(base_path.glob(old_base + '.*'))
        if not matched_files:
            print(f"- [SKIP] No file found matching base name '{old_base}'")
            continue
        for old_file in matched_files:
            new_file = old_file.with_name(f"{new_base}{old_file.suffix}")
            if new_file.exists():
                print(f"- [SKIP] Target filename {new_file.name} already exists; leaving {old_file.name} unchanged.")
                continue
            try:
                old_file.rename(new_file)
                print(f"- [OK] Renamed '{old_file.name}' to '{new_file.name}'")
            except Exception as e:
                print(f"- [ERROR] Failed to rename '{old_file.name}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_notebooks.py <directory>")
    else:
        main(sys.argv[1])
