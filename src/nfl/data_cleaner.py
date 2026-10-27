import pandas as pd
import nflreadpy as nfl


class DataCleaner():

    def load_data():
        pbp = nfl.load_pbp(
            seasons=[2020,2021,2022,2023,2024,2025,2026]
        )
        
        pbp = pbp.to_pandas()

        return pbp

    def clean_data(pbp):
        pbp = pbp[['posteam', 'defteam', 'qtr', 'quarter_seconds_remaining', 'down', 'ydstogo', 'posteam_score', 'defteam_score', 'home_team', 'away_team', 'week','yardline_100', 'play_type']]
        pbp = pbp.loc[pbp['play_type'].isin(['pass', 'run'])]
        
        return pbp

    def encode(pbp):
        # encode home team and posteam/defteam to be the same
        teams = set(pbp["home_team"]) | (set(pbp["away_team"]) | (set(pbp["posteam"])) | (set(pbp["defteam"])))
        teams = sorted(teams)

        team_to_id = {}

        for i, team in enumerate(teams):
            team_to_id[team] = i
        
        pbp["HomeTeamID"] = pbp["home_team"].map(team_to_id)
        pbp["AwayTeamID"] = pbp["away_team"].map(team_to_id)
        pbp["posteamID"] = pbp["posteam"].map(team_to_id)
        pbp["defteamID"] = pbp["defteam"].map(team_to_id)

        # encode result pass = 1 run = 0
        result = {
            'pass': 1,
            'run': 0
        }

        pbp["result"] = pbp["play_type"].map(result)

        return pbp

    def features(pbp):
        # in redzone 0/1 (no/yes), score differential,  
        
        pbp["in_redzone"] = (pbp["yardline_100"] <= 20).astype(int)

        pbp["score_diff"] = (pbp["posteam_score"] - pbp["defteam_score"])
        
        return pbp

        
        
    
    


