# 🔍 DataLens — Automated EDA & Data Cleaning Tool

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-3.x-yellow.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-orange.svg)](https://seaborn.pydata.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.17-red.svg)](https://scipy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

A production-grade, browser-based **Automated Exploratory Data Analysis (EDA)** tool built with **Flask**, **Pandas**, **Seaborn**, and **SciPy**. Upload any CSV dataset and instantly receive a comprehensive statistical report with interactive visualizations, outlier detection, and automated data cleaning — all in a sleek dark-themed UI.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 📊 **Dataset Overview** | Instant summary of rows, columns, duplicates, and missing values |
| 📈 **Distribution Plots** | Auto-generated KDE + histogram plots for up to 6 numerical features |
| 🔥 **Correlation Heatmap** | Annotated Pearson correlation matrix across all numerical columns |
| 🎯 **Outlier Detection** | Z-score based outlier identification (threshold > 3σ) per column |
| 📉 **Missing Value Analysis** | Visual bar chart and per-column missing percentage breakdown |
| 🧹 **Automated Data Cleaning** | Median imputation for missing numerics + duplicate removal |
| 🌙 **Premium Dark UI** | Glassmorphism, gradient accents, micro-animations, and responsive design |
| 📂 **Drag & Drop Upload** | Drag CSV files directly into the browser or click to browse |

---

## 🏗️ Project Structure

```
DataLens/
├── app.py              # Flask server with upload & EDA endpoint
├── eda_engine.py       # Core EDA logic: stats, plots, outliers, cleaning
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── templates/
│   └── index.html      # Premium dark-theme frontend
├── static/
│   └── style.css       # Glassmorphism CSS design system
└── uploads/            # Auto-created directory for uploaded CSVs
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AyushMishra-02/DataLens.git
cd DataLens
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
Navigate to **http://localhost:5000**, upload any CSV file, and click **"Run EDA Analysis"**.

---

## 📊 What the Report Includes

### Dataset Overview Panel
Displays key statistics at a glance:
- **Total Rows & Columns** — Dataset dimensions
- **Duplicate Count** — Number of exact duplicate rows detected
- **Rows After Cleaning** — Final row count after median imputation + deduplication
- **Columns with Missing** — Number of features containing null values
- **Total Outliers** — Aggregate count of statistical outliers (z-score > 3)

### Missing Values & Outliers Table
A detailed per-column breakdown showing:
- Column name and data type
- Missing value count with color-coded severity badges
- Missing percentage
- Outlier count per feature using z-score methodology

### Feature Distribution Plots
Auto-generated **histogram + KDE overlay** plots for up to 6 numerical features, providing instant insight into data distributions, skewness, and modality.

### Correlation Heatmap
An annotated **Pearson correlation matrix** rendered as a heatmap, highlighting linear relationships between all numerical variables.

---

## ⚙️ How the EDA Engine Works

The core analysis pipeline in `eda_engine.py` performs the following steps:

1. **Data Ingestion** — Reads the uploaded CSV using Pandas
2. **Schema Analysis** — Extracts column names, data types, and shape
3. **Missing Value Audit** — Counts nulls per column with percentage calculations
4. **Descriptive Statistics** — Generates `describe()` summary for numerical features
5. **Outlier Detection** — Applies **z-score analysis** (threshold: |z| > 3) per numerical column using SciPy
6. **Visualization Generation** — Creates distribution histograms, correlation heatmaps, and missing value charts using Matplotlib & Seaborn, encoded as inline base64 PNG images
7. **Automated Cleaning** — Applies **median imputation** for missing numerical values and removes duplicate rows

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.11, Flask |
| **Data Processing** | Pandas, NumPy |
| **Statistical Analysis** | SciPy (z-score outlier detection) |
| **Visualization** | Matplotlib (Agg backend), Seaborn |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Design** | Dark theme, CSS Grid, Glassmorphism, CSS animations |

---

## 📁 Supported Datasets

DataLens works with any well-formed CSV file. Some recommended test datasets:

| Dataset | Source | Columns | Rows |
| :--- | :--- | :---: | :---: |
| Titanic | [Kaggle](https://www.kaggle.com/c/titanic) | 12 | 891 |
| California Housing | scikit-learn | 9 | 20,640 |
| Iris | scikit-learn | 5 | 150 |
| Heart Disease | [UCI ML](https://archive.ics.uci.edu/) | 14 | 303 |

---

## 📝 API Reference

### `GET /`
Returns the main HTML page with the upload interface.

### `POST /upload`
Accepts a CSV file via `multipart/form-data` and returns a JSON EDA report.

**Request:**
```
Content-Type: multipart/form-data
Body: file=<your_dataset.csv>
```

**Response (JSON):**
```json
{
  "shape": [891, 12],
  "columns": ["PassengerId", "Survived", ...],
  "dtypes": {"PassengerId": "int64", ...},
  "missing": {"Age": 177, "Cabin": 687, ...},
  "missing_pct": {"Age": 19.87, "Cabin": 77.1, ...},
  "duplicates": 0,
  "stats": { ... },
  "outliers": {"Age": 1, "Fare": 116, ...},
  "dist_imgs": {"Age": "<base64_png>", ...},
  "heatmap": "<base64_png>",
  "missing_plot": "<base64_png>",
  "cleaned_shape": [891, 12]
}
```

---

## 👤 Author

**Ayush Mishra** — ML Summer School 2026

---

## 📄 License

This project is licensed under the MIT License.
