
import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(
    os.path.join(BASE_DIR, "model_best.joblib")
)

# =========================================================
# LOAD SCALER
# =========================================================

scaler_data = joblib.load(
    os.path.join(BASE_DIR, "scaler.joblib")
)

scaler = scaler_data["scaler"]

# IMPORTANT:
# Use the exact columns the scaler was fitted with
scaler_features = list(scaler.feature_names_in_)

# Exact columns expected by the model
model_features = list(model.feature_names_in_)


# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict(input_dict):

    # -----------------------------------------------------
    # Create input data
    # -----------------------------------------------------

    df = pd.DataFrame([{
        "number_of_bedrooms": input_dict["number_of_bedrooms"],
        "number_of_bathrooms": input_dict["number_of_bathrooms"],
        "number_of_floors": input_dict["number_of_floors"],
        "living_area": input_dict["living_area"],
        "lot_area": input_dict["lot_area"],
        "condition_of_the_house": input_dict["condition_of_the_house"],
        "postal_code": input_dict["postal_code"],
        "latitude": input_dict["latitude"],
        "longitude": input_dict["longitude"],
        "number_of_schools_nearby": input_dict["number_of_schools_nearby"],
        "built_year": input_dict["built_year"],
        "house_age": input_dict["house_age"]
    }])

    # -----------------------------------------------------
    # SCALE EXACTLY THE SAME FEATURES USED DURING TRAINING
    # -----------------------------------------------------

    df[scaler_features] = scaler.transform(
        df[scaler_features]
    )

    # -----------------------------------------------------
    # CITY ONE-HOT ENCODING
    # -----------------------------------------------------

    df["city_Ghaziabad"] = 0
    df["city_Gurgaon"] = 0
    df["city_Noida"] = 0

    # Get city from input
    city = input_dict.get("city", "")

    if city == "Ghaziabad":
        df["city_Ghaziabad"] = 1

    elif city == "Gurgaon":
        df["city_Gurgaon"] = 1

    elif city == "Noida":
        df["city_Noida"] = 1

    # -----------------------------------------------------
    # ARRANGE EXACTLY AS MODEL EXPECTS
    # -----------------------------------------------------

    df = df[model_features]

    # -----------------------------------------------------
    # PREDICT
    # -----------------------------------------------------

    prediction = model.predict(df)[0]

    return prediction

