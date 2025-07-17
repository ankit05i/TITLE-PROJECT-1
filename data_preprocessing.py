import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    print("Initial data shape:", df.shape)
    df.dropna(inplace=True)
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['hour'] = df['date_time'].dt.hour
    df['day_of_week'] = df['date_time'].dt.dayofweek
    df = df.drop(['date_time'], axis=1, errors='ignore')
    return df

if __name__ == "__main__":
    data = load_and_clean_data("../data/traffic_data.csv")
    print(data.head())
    data.to_csv("../data/cleaned_traffic_data.csv", index=False)
    print("Cleaned data saved.")
