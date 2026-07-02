import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# LOAD EXCEL FILE
df = pd.read_excel("2000-22.xlsx")

# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip()

print(df.columns)

# TARGET COLUMN
TARGET_COLUMN = "total_cognizable_crimes_under_ipc"

# CREATE YEAR COLUMN
if "Year" not in df.columns:
    df["Year"] = df["year"]

# CREATE STATE COLUMN
df["State"] = "India"

# CREATE CRIME TYPE COLUMN
df["Crime Type"] = "Total IPC"

# ENCODERS
state_encoder = LabelEncoder()
crime_encoder = LabelEncoder()

df["State"] = state_encoder.fit_transform(df["State"])
df["Crime Type"] = crime_encoder.fit_transform(df["Crime Type"])

# FEATURES
X = df[["State", "Year", "Crime Type"]]

# TARGET
y = df[TARGET_COLUMN]

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestRegressor()

model.fit(X_train, y_train)

# SAVE
joblib.dump(model, "models/crime_model.pkl")
joblib.dump(state_encoder, "models/state_encoder.pkl")
joblib.dump(crime_encoder, "models/crime_encoder.pkl")

print("Model Trained Successfully")