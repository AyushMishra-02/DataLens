import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os, base64
from io import BytesIO

def fig_to_base64():
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=120, bbox_inches='tight')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img

def run_eda(filepath):
    df = pd.read_csv(filepath)
    report = {}

    # Basic info
    report['shape'] = df.shape
    report['columns'] = list(df.columns)
    report['dtypes'] = df.dtypes.astype(str).to_dict()
    report['missing'] = df.isnull().sum().to_dict()
    report['missing_pct'] = (df.isnull().mean() * 100).round(2).to_dict()
    report['duplicates'] = int(df.duplicated().sum())

    # Stats
    num_df = df.select_dtypes(include=np.number)
    report['stats'] = num_df.describe().round(3).to_dict()

    # Outlier detection (z-score)
    outliers = {}
    for col in num_df.columns:
        z = np.abs(stats.zscore(num_df[col].dropna()))
        outliers[col] = int((z > 3).sum())
    report['outliers'] = outliers

    # Distribution plots
    dist_imgs = {}
    for col in num_df.columns[:6]:  # limit to 6 for speed
        plt.figure(figsize=(6, 3))
        sns.histplot(df[col].dropna(), kde=True, color='steelblue')
        plt.title(f'Distribution: {col}')
        plt.tight_layout()
        dist_imgs[col] = fig_to_base64()
    report['dist_imgs'] = dist_imgs

    # Correlation heatmap
    if len(num_df.columns) > 1:
        plt.figure(figsize=(10, 7))
        sns.heatmap(num_df.corr(), annot=True, fmt='.2f',
                    cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        report['heatmap'] = fig_to_base64()

    # Missing values bar
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        plt.figure(figsize=(8, 4))
        missing.plot(kind='bar', color='tomato', edgecolor='black')
        plt.title('Missing Values per Column')
        plt.ylabel('Count')
        plt.tight_layout()
        report['missing_plot'] = fig_to_base64()

    # Data cleaning
    df_clean = df.copy()
    for col in num_df.columns:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)
    df_clean.drop_duplicates(inplace=True)
    report['cleaned_shape'] = df_clean.shape

    return report, df_clean
