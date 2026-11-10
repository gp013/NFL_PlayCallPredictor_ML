from data_cleaner import DataCleaner
from model import Model
from sklearn.model_selection import train_test_split
import pandas as pd

class Features:

    def get_team() -> int:
        team = input("Team ID (ex: ARI for Arizona): ")

        teams = {
            "ARI": 0,
            "Arizona": 0,
            "ATL": 1,
            "Atlanta": 1,
            "BAL": 2,
            "Baltimore": 2,
            "BUF": 3,
            "Buffalo": 3,
            "CAR": 4,
            "Carolina": 4,
            "CHI": 5,
            "Chicago": 5,
            "CIN": 6,
            "Cincinnati": 6,
            "CLE": 7,
            "Cleveland": 7,
            "DAL": 8,
            "Dallas": 8,
            "DEN": 9,
            "Denver": 9,
            "DET": 10,
            "Detroit": 10,
            "GB": 11,
            "Green Bay": 11,
            "HOU": 12,
            "Houston": 12,
            "IND": 13,
            "Indianapolis": 13,
            "JAX": 14,
            "Jacksonville": 14,
            "KC": 15,
            "Kansas City": 15,
            "LV": 16,
            "Las Vegas": 16,
            "LAC": 17,
            "Los Angeles Chargers": 17,
            "LA": 18,
            "Los Angeles Rams": 18,
            "MIA": 19,
            "Miami": 19,
            "MIN": 20,
            "Minnesota": 20,
            "NE": 21,
            "New England": 21,
            "NO": 22,
            "New Orleans": 22,
            "NYG": 23,
            "New York Giants": 23,
            "NYJ": 24,
            "New York Jets": 24,
            "PHI": 25,
            "Philadelphia": 25,
            "PIT": 26,
            "Pittsburgh": 26,
            "SF": 27,
            "San Francisco": 27,
            "SEA": 28,
            "Seattle": 28,
            "TB": 29,
            "Tampa Bay": 29,
            "TEN": 30,
            "Tennesee": 30,
            "WAS": 31,
            "Washington": 31
        }

        team_id = teams[team]
        
        return team_id

    def train_on_team(team_id: int, pbp: pd.DataFrame) -> float:
        model = Model()
        
        pbp = pbp.loc[pbp["posteamID"] == team_id]
        

        X, y = DataCleaner.X_y_split(pbp)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, train_size =0.8, random_state=42
        )
        model.train(X_train, y_train)

        accuracy = model.evaluate(X_test, y_test)

        return accuracy

    def most_predictable(pbp: pd.DataFrame) -> None:
        model = Model()

        teams = {
            0: "ARI",
            1: "ATL",
            2: "BAL",
            3: "BUF",
            4: "CAR",
            5: "CHI",
            6: "CIN",
            7: "CLE",
            8: "DAL",
            9: "DEN",
            10: "DET",
            11: "GB",
            12: "HOU",
            13: "IND",
            14: "JAX",
            15: "KC",
            16: "LV",
            17: "LAC",
            18: "LA",
            19: "MIA",
            20: "MIN",
            21: "NE",
            22: "NO",
            23: "NYG",
            24: "NYJ",
            25: "PHI",
            26: "PIT",
            27: "SF",
            28: "SEA",
            29: "TB",
            30: "TEN",
            31: "WAS"
        }
        
        try:
            with open("predicts.txt", "r") as f:
                percentages = []
                teams = []
                
                for line in f:

                    text = line.strip()
                    num = float(text.split(":")[1])
                    team = text.split(":")[0].strip()
                    percentages.append(num)
                    teams.append(team)

                min_percentage = min(percentages)
                max_percentage = max(percentages)
                avg_percentage = sum(percentages) / len(percentages)
                min_index = percentages.index(min_percentage)
                max_index = percentages.index(max_percentage)

                print(f"Highest prediction percentage: {teams[max_index]} {percentages[max_index]:.2f}%")
                print(f"Lowest prediction percentage: {teams[min_index]} {percentages[min_index]:.2f}%")
                print(f"Average prediction percentage: {avg_percentage:.2f}%")

                f.close()
                
        except FileNotFoundError:
            with open("predicts.txt", "w") as f:
                for i in range (0,32):
                    team = teams[i] 
                    df = pbp.loc[pbp["posteamID"] == i]
                    
                    X, y = DataCleaner.X_y_split(df)
                    
                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, train_size =0.8, random_state=42
                    )
                    model.train(X_train, y_train)

                    accuracy = model.evaluate(X_test, y_test)
                    accuracy *= 100

                    f.write(team + ": " + str(accuracy) + "\n")

                f.close()
            
            with open("predicts.txt", "r") as f:
                percentages = []
                teams = []
                
                for line in f:

                    text = line.strip()
                    num = float(text.split(":")[1])
                    team = text.split(":")[0].strip()
                    percentages.append(num)
                    teams.append(team)

                min_percentage = min(percentages)
                max_percentage = max(percentages)
                min_index = percentages.index(min_percentage)
                max_index = percentages.index(max_percentage)

                print(f"Highest prediction percentage: {teams[max_index]} {percentages[max_index]:.2f}%")
                print(f"Lowest prediction percentage: {teams[min_index]} {percentages[min_index]:.2f}%")

                f.close()
    
    
    def live_game(pbp, model):
        
        
        # Get Variables for features
        week: int = int(input("Week: "))
        print("Home Team")
        homeID: int = Features.get_team()
        print("Away Team")
        awayID: int = Features.get_team()
        home_score: float = float(input("Home team score: "))
        away_score: float = float(input("Away team score: "))

        qtr: float = float(input("Quarter: "))
        time: str = input("Time in game (format of 15:00): ")
        possession: str = input("Possesion (h for home, a for away): ")
        yardline: float = float(input("Yards from endzone: "))
        down: float = float(input("Down: "))
        ydstogo: float = float(input("Yards to first down: "))

        
        

        # format into float/int data types

        minutes = float(time.split(":")[0]) * 60
        seconds = float(time.split(":")[1])

        seconds += minutes

        if possession == "h":
            posteamID = homeID
            posteam_score = home_score
            defteamID = awayID
            defteam_score = away_score

            score_diff = float(posteam_score) - float(defteam_score)

        elif possession == "a":
            posteamID = awayID
            posteam_score = away_score
            defteamID = homeID
            defteam_score = home_score

            score_diff = float(posteam_score) - float(defteam_score)

        else:
            print("Invalid possession option")
        
        if float(yardline) <= 20:
            redzone = 1
        else:
            redzone = 0

        # [["HomeTeamID", "AwayTeamID", "posteamID", "defteamID", "qtr", "quarter_seconds_remaining", "down", "ydstogo", "posteam_score", "defteam_score", "week", "yardline_100", "in_redzone", "score_diff"]]
        # homeID, awayID, posteamID, defteamID, qtr, seconds, down, ydstogo, posteam score, defteam_score, week, yardline, redzone, score_diff 
        #data = [homeID, awayID, posteamID, defteamID, qtr, seconds, down, ydstogo, posteam_score, defteam_score, week, yardline, redzone, score_diff]
       
        data = pd.DataFrame([[homeID, awayID, posteamID, defteamID, qtr, seconds, down, ydstogo, posteam_score, defteam_score, week, yardline, redzone, score_diff]])
        data.columns = ["HomeTeamID", "AwayTeamID", "posteamID", "defteamID", "qtr", "quarter_seconds_remaining", "down", "ydstogo", "posteam_score", "defteam_score", "week", "yardline_100", "in_redzone", "score_diff"]

        prediction = model.predict(data)

        if prediction[0] == 0:
            play = "Run"
        else: 
            play ="Pass"
        
        print(prediction)

        key = False

        while(key != True):
            option = int(input("Exit? (1 to exit, 2 to continue): "))
            
            if option == 1:
                key = True
                break
            
            change_of_pos = int(input("Change of possession? (1 for yes, 2 for no): "))
            
            if change_of_pos == 1:
                score_change = int(input("Did the play end in a score? (1 for yes, 2 for no): "))
                if score_change == 1:
                    score = float(input("How much did possession team score: "))
                    posteam_score += score
                                    
                posteamID, defteamID = defteamID, posteamID
                score_diff = float(posteam_score - defteam_score)
            

                #Time update
            prev_seconds = seconds
            time = input("Update Time(format 15:00): ")
            minutes = float(time.split(":")[0]) * 60
            seconds = float(time.split(":")[1])
            seconds += minutes

            # qtr update if needed
            if seconds > prev_seconds:
                qtr += 1

            # Yardline, down, ydstogo update
            yards_gained = float(input("Yards gained on previous play: "))
            if yards_gained >= ydstogo:
                ydstogo = 10
                down = 1
                yardline -= yards_gained
                print(ydstogo, down, yardline)
            else:
                down += 1
                ydstogo -= yards_gained
                yardline -= yards_gained
                print(ydstogo, down, yardline)
                
            # redzone update
            if float(yardline) <= 20:
                redzone = 1
            else:
                redzone = 0

            data = pd.DataFrame([[homeID, awayID, posteamID, defteamID, qtr, seconds, down, ydstogo, posteam_score, defteam_score, week, yardline, redzone, score_diff]])
            data.columns = ["HomeTeamID", "AwayTeamID", "posteamID", "defteamID", "qtr", "quarter_seconds_remaining", "down", "ydstogo", "posteam_score", "defteam_score", "week", "yardline_100", "in_redzone", "score_diff"]
            
            prediction = model.predict(data)

            if prediction[0] == 0:
                play = "Run"
            else: 
                play ="Pass"
        
            print(play)