import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('../plots', exist_ok=True)

def plot_race_winners_over_years(race_summaries):
    plt.figure(figsize=(14, 7))
    sns.countplot(x='Year', data=race_summaries, palette='viridis')
    plt.title('Distribution of Race Winners Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Races')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../plots/race_winners_over_years.png')
    plt.close()

def plot_top_drivers_by_points(driver_standings):
    top_drivers = driver_standings.groupby('Driver').sum()['PTS'].sort_values(ascending=False).head(10)
    plt.figure(figsize=(14, 7))
    sns.barplot(x=top_drivers.index, y=top_drivers.values, palette='rocket')
    plt.title('Top 10 Drivers by Total Points')
    plt.xlabel('Driver')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../plots/top_drivers_by_points.png')
    plt.close()