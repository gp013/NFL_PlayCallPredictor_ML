# NFL_PlayCallPredictor_ML
Using a XGBoost Model, it takes in the last 4 years of play-by-play data in the NFL, trains a XGBoost model on whether the play will be a run or a pass. Initially trained on all plays it reached a max of 72% prediction accuracy. This program also contains features on training on a certain team or predicting plays from a single game. 
Parameters of model:["HomeTeamID", "AwayTeamID", "posteamID", "defteamID", "qtr", "quarter_seconds_remaining", "down", "ydstogo", "posteam_score", "defteam_score", "week", "yardline_100", "in_redzone", "score_diff"]
To gain these features I used pandas to clean the data and create features such as in_redzone and score_diff.
