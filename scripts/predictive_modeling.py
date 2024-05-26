# scripts/predictive_modeling.py

import json
import pandas as pd  # Import pandas library
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def predictive_modeling(merged_df):
    # Convert 'Pos' column to numeric type
    merged_df['Pos'] = pd.to_numeric(merged_df['Pos'], errors='coerce')

    # Predicting if a driver finishes in top 3
    merged_df['Top3Finish'] = merged_df['Pos'].apply(lambda x: 1 if x <= 3 else 0)

    # Selecting features and target
    features = ['Pos_grid', 'TotalPitstops', 'AvgQualifyingTime']
    X = merged_df[features]
    y = merged_df['Top3Finish']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    importances = model.feature_importances_

    # Save report
    report_data = {
        'accuracy': accuracy,
        'classification_report': report,
        'feature_importances': dict(zip(features, importances))
    }

    with open('../data/f1_report.json', 'w') as f:
        json.dump(report_data, f, indent=4)

    return model, features, importances
