from data_cleaner import DataCleaner


pbp = DataCleaner.load_data()

pbp = DataCleaner.clean_data(pbp)
pbp = DataCleaner.encode(pbp)
pbp = DataCleaner.features(pbp)

pbp.to_csv("DATA.csv")

X, y = DataCleaner.X_y_split(pbp)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.train(X_train, y_train)

accuracy = model.evaluate(X_test, y_test)

print(accuracy)
