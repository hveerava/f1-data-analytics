# scripts/visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the plots directory exists
os.makedirs('../plots', exist_ok=True)

def plot_feature_importance(importances, features):
    indices = importances.argsort()[::-1]
    plt.figure(figsize=(14, 7))
    plt.title('Feature Importances')
    plt.bar(range(len(features)), importances[indices], align='center')
    plt.xticks(range(len(features)), [features[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.savefig('../plots/feature_importances.png')
    plt.close()

def plot_top_constructors_by_wins(constructor_standings):
    top_constructors = constructor_standings.groupby('Team').sum()['PTS'].sort_values(ascending=False).head(10)
    plt.figure(figsize=(14, 7))
    sns.barplot(x=top_constructors.index, y=top_constructors.values, palette='magma')
    plt.title('Top 10 Constructors by Total Points')
    plt.xlabel('Constructor')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../plots/top_constructors_by_points.png')
    plt.close()


def plot_correlation_matrix(correlation_matrix, save_path=None):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='magma')
    plt.title('Correlation Matrix')
    if save_path:
        plt.savefig(save_path)
    plt.show()
