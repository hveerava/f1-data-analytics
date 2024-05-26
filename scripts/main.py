import load_data
import eda
import feature_engineering
import predictive_modeling
import hyperparameter_tuning
import visualizations
import win_prediction
from sklearn.model_selection import train_test_split

# Load data
data = load_data.load_data()

# EDA
eda.plot_race_winners_over_years(data['race_summaries'])
eda.plot_top_drivers_by_points(data['driver_standings'])

# Feature Engineering
merged_df = feature_engineering.feature_engineering(
    data['pitstops'], 
    data['qualifyings'], 
    data['race_details'], 
    data['starting_grids'], 
    data['sprint_results'], 
    data['fastestlaps_detailed']
)

# Predictive Modeling
model, features, importances = predictive_modeling.predictive_modeling(merged_df)

# Hyperparameter Tuning
X_train, X_test, y_train, y_test = train_test_split(merged_df[features], merged_df['Top3Finish'], test_size=0.2, random_state=42)
best_params = hyperparameter_tuning.hyperparameter_tuning(X_train, y_train)

# Additional Visualizations
visualizations.plot_feature_importance(importances, features)
visualizations.plot_top_constructors_by_wins(data['constructor_standings'])

# Correlation Matrix
correlation_matrix = win_prediction.generate_correlation_matrix(data['race_summaries'])
win_prediction.plot_correlation_matrix(correlation_matrix, save_path='../plots/driver_vs_gp_correlation.png')