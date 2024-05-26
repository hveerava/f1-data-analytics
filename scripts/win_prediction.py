import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_correlation_matrix(data):
    driver_gp_frequency = data.groupby(['Car', 'Grand Prix']).size().unstack(fill_value=0)

    return driver_gp_frequency

def plot_correlation_matrix(correlation_matrix, save_path=None):
    plt.figure(figsize=(20, 20))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Driver vs. Grand Prix Frequency')
    plt.xlabel('Grand Prix')
    plt.ylabel('Driver')
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
