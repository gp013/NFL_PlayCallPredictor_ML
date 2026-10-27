from data_cleaner import DataCleaner


pbp = DataCleaner.load_data()

pbp = DataCleaner.clean_data(pbp)
pbp = DataCleaner.encode(pbp)
pbp = DataCleaner.features(pbp)

pbp.to_csv("DATA.csv")
