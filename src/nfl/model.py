from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

class Model():

    def __init__(self):
         self.model = XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42,
            eval_metric="logloss",
            n_jobs=-1
        )
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
    
    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        return accuracy_score(y_test, predictions)

    
