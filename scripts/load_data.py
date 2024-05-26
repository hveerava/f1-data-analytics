# scripts/load_data.py

import pandas as pd
import os

def load_data():
    # Determine the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the data directory
    data_path = os.path.join(script_dir, '..', 'data')

    race_details = pd.read_csv(os.path.join(data_path, 'race_details.csv'))
    race_summaries = pd.read_csv(os.path.join(data_path, 'race_summaries.csv'))
    starting_grids = pd.read_csv(os.path.join(data_path, 'starting_grids.csv'))
    sprint_grid = pd.read_csv(os.path.join(data_path, 'sprint_grid.csv'))
    sprint_results = pd.read_csv(os.path.join(data_path, 'sprint_results.csv'))
    fastest_laps = pd.read_csv(os.path.join(data_path, 'fastest_laps.csv'))
    fastestlaps_detailed = pd.read_csv(os.path.join(data_path, 'fastestlaps_detailed.csv'))
    qualifyings = pd.read_csv(os.path.join(data_path, 'qualifyings.csv'))
    practices = pd.read_csv(os.path.join(data_path, 'practices.csv'))
    pitstops = pd.read_csv(os.path.join(data_path, 'pitstops.csv'))
    team_details = pd.read_csv(os.path.join(data_path, 'team_details.csv'))
    constructor_standings = pd.read_csv(os.path.join(data_path, 'constructor_standings.csv'))
    driver_standings = pd.read_csv(os.path.join(data_path, 'driver_standings.csv'))
    driver_details = pd.read_csv(os.path.join(data_path, 'driver_details.csv'))

    return {
        'race_details': race_details,
        'race_summaries': race_summaries,
        'starting_grids': starting_grids,
        'sprint_grid': sprint_grid,
        'sprint_results': sprint_results,
        'fastest_laps': fastest_laps,
        'fastestlaps_detailed': fastestlaps_detailed,
        'qualifyings': qualifyings,
        'practices': practices,
        'pitstops': pitstops,
        'team_details': team_details,
        'constructor_standings': constructor_standings,
        'driver_standings': driver_standings,
        'driver_details': driver_details
    }
