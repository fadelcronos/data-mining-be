import json
import joblib
import pandas as pd
import numpy as np

# config file
fileConfig = open("config/config.json")
config = json.load(fileConfig)
rf = joblib.load("c45.joblib")

def validateUserData(data):
    if (data["property_area"] == "URBAN"):
        print("MASUK CUK")
        property_area_rural = "0"
        property_area_semi_urban = "0"
        property_area_urban = "1"
    elif(data["property_area"] == "SEMI_URBAN"):
        property_area_rural = "0"
        property_area_semi_urban = "1"
        property_area_urban = "0"
    else:
        property_area_rural = "1"
        property_area_semi_urban = "0"
        property_area_urban = "0"

    if (data["dependents"] == "0"):
        dp0 = "1"
        dp1 = "0"
        dp2 = "0"
        dp3 = "0"
    elif (data["dependents"] == "1"):
        dp0 = "0"
        dp1 = "1"
        dp2 = "0"
        dp3 = "0"
    elif (data["dependents"] == "2"):
        dp0 = "0"
        dp1 = "0"
        dp2 = "1"
        dp3 = "0"
    else:
        dp0 = "0"
        dp1 = "0"
        dp2 = "0"
        dp3 = "1"

    dsData = {
        "ApplicantIncome": data["applicant_income"],
        "CoapplicantIncome": data["coapplicant_income"],
        "LoanAmount": data["loan_amount"],
        "Loan_Amount_Term": data["loan_amount_term"],
        "Credit_History": data["credit_history"],
        "Gender": data["gender"],
        "Married": data["married"],
        "Dependents_0": dp0,
        "Dependents_1": dp1,
        "Dependents_2": dp2,
        "Dependents_3+": dp3,
        "Education": data["education"],
        "Self_Employed": data["self_employed"],
        "Property_Area_Rural": property_area_rural,
        "Property_Area_Semiurban": property_area_semi_urban,
        "Property_Area_Urban": property_area_urban
    }

    ds = pd.json_normalize(dsData)
    # print(ds)
    # print(type(ds))
    eligibileStatus = rf.predict(ds)
    res = np.ndarray.tolist(eligibileStatus)

    if (res[0] == 1):
        result = {"Eligible": "Y"}
    else:
        result = {"Eligible": "N"}

    return result