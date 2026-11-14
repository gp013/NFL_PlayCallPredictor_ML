from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

class Model:

    def __init__(self) -> None :
         self.model = XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42,
            eval_metric="logloss",
            n_jobs=-1
        )
    
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X_test)
    
    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> float:
        predictions = self.predict(X_test)
        return accuracy_score(y_test, predictions)

    
