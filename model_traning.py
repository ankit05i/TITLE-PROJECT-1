import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(filepath):
    df = pd.read_csv(filepath)
    X = df[['hour', 'day_of_week', 'weather_code']]
    y = df['traffic_volume']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model MAE: {mae}")
    joblib.dump(model, "../src/traffic_model.pkl")
    print("Model saved as traffic_model.pkl")

if __name__ == "__main__":
    train_model("../data/cleaned_traffic_data.csv")
