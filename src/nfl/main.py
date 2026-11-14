from data_cleaner import DataCleaner
from features import Features
from model import Model
from sklearn.model_selection import train_test_split

def main():

    model = Model()

    pbp = DataCleaner.load_data()
    pbp = DataCleaner.clean_data(pbp)
    pbp = DataCleaner.encode(pbp)
    pbp = DataCleaner.features(pbp)

    X, y = DataCleaner.X_y_split(pbp)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, train_size =0.8, random_state=42
    )
    model.train(X_train, y_train)
    accuracy = model.evaluate(X_test, y_test)

    Features.set_predicts(pbp)




    while(True):
        print("NFL pbp Machine Learning")
        print(" ")
        print("1) Accuracy of Model on all teams")
        print("2) Specific team training")
        print("3) Highest, Lowest & Average prediction percentages")
        print("4) All team percentages")
        print("5) Live game predictions")
        print("6) Exit")

        key = int(input("Choose an option: "))
        print(" ")

        if key == 1:
            print(f"Total Model Accuracy: {accuracy}%")
        elif key == 2:
            team = Features.get_team()
            team_acc = Features.train_on_team(team, pbp)
            print(team_acc)
        elif key == 3:
            Features.most_predictable(pbp)
        elif key == 4:
            Features.get_all_teams()
        elif key == 5:
            Features.live_game(pbp, model)
        elif key == 6:
            break

        print(" ")



if __name__ == "__main__":
    main()
