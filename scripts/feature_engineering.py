import pandas as pd

def preprocess_qualifying_times(qualifyings):
    for col in ['Q1', 'Q2', 'Q3']:
        qualifyings[col] = qualifyings[col].str.extract(r'(\d+:\d+\.\d+)', expand=False) 
        qualifyings[col] = qualifyings[col].str.replace(':', '').astype(float) / 1000  

    return qualifyings

def feature_engineering(pitstops, qualifyings, race_details, starting_grids, sprint_results, fastestlaps_detailed):
    qualifyings[['Q1', 'Q2', 'Q3']] = qualifyings[['Q1', 'Q2', 'Q3']].fillna(0)

    qualifyings = preprocess_qualifying_times(qualifyings)

    qualifyings['AvgQualifyingTime'] = qualifyings[['Q1', 'Q2', 'Q3']].mean(axis=1)

    pitstops['TotalPitstops'] = pitstops.groupby(['Year', 'Grand Prix', 'Driver'])['Stops'].transform('sum')

    merged_df = race_details.merge(starting_grids, on=['Year', 'Grand Prix', 'Driver'], suffixes=('', '_grid'))
    merged_df = merged_df.merge(sprint_results, on=['Year', 'Grand Prix', 'Driver'], suffixes=('', '_sprint'))
    merged_df = merged_df.merge(fastestlaps_detailed, on=['Year', 'Grand Prix', 'Driver'], suffixes=('', '_fastlap'))
    merged_df = merged_df.merge(qualifyings[['Year', 'Grand Prix', 'Driver', 'AvgQualifyingTime']], 
                                 on=['Year', 'Grand Prix', 'Driver'], how='left')
    merged_df = merged_df.merge(pitstops[['Year', 'Grand Prix', 'Driver', 'TotalPitstops']], 
                                 on=['Year', 'Grand Prix', 'Driver'], how='left')
    
    return merged_df
