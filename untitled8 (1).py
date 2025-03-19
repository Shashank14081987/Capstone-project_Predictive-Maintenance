# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qh9Sksd_FU0-A9DvZzwbG6G8EsqJwPYx
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, BaggingRegressor, StackingRegressor, VotingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

# Load dataset
df = pd.read_csv("predictive_maintenance.csv")
df

# prompt: code for describe function

def describe_data(df):
  """
  Provides a comprehensive overview of the dataset, including:
    - Shape (rows, columns)
    - Data types of each column
    - Descriptive statistics (count, mean, std, min, max, etc.)
    - Missing value counts
    - Unique values for categorical features
  """
  print("Shape:", df.shape)
  print("\nData Types:\n", df.dtypes)
  print("\nDescriptive Statistics:\n", df.describe(include='all'))
  print("\nMissing Values:\n", df.isnull().sum())

  for col in df.columns:
    if df[col].dtype == 'object':
      print(f"\nUnique values for {col}:\n{df[col].unique()}")


describe_data(df)

print(df.isnull().sum())

def describe_data(df):
  """
  Provides a comprehensive overview of the dataset, including:
    - Shape (rows, columns)
    - Data types of each column
    - Descriptive statistics (count, mean, std, min, max, etc.)
    - Missing value counts
    - Unique values for categorical features
  """
  print("Shape:", df.shape)
  print("\nData Types:\n", df.dtypes)
  print("\nDescriptive Statistics:\n", df.describe(include='all'))
  print("\nMissing Values:\n", df.isnull().sum())

  for col in df.columns:
    if df[col].dtype == 'object':
      print(f"\nUnique values for {col}:\n{df[col].unique()}")


describe_data(df)

# prompt: generate code to plot bar chart against each variable

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame
for column in df.columns:
  if df[column].dtype in ['int64', 'float64']:  # Check if the column is numeric
    plt.figure(figsize=(15, 6))
    sns.barplot(x=df[column].value_counts().index, y=df[column].value_counts().values)
    plt.title(f'Bar Chart for {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.show()

# Drop irrelevant columns
df = df.drop(columns=["UDI", "Product ID"])
df

# Encode categorical variable 'Type'
label_encoder = LabelEncoder()
df["Type"] = label_encoder.fit_transform(df["Type"])

# Define features and target
X = df.drop(columns=["Target"])
y = df["Target"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train

X_test

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Import necessary libraries
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier, BaggingClassifier, StackingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Define models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Ada Boost": AdaBoostClassifier(random_state=42),
    "Gradient Boost": GradientBoostingClassifier(random_state=42),
    "LGBMR": LGBMClassifier(random_state=42),
    "XGBR": XGBClassifier(random_state=42),
    "SVM": SVC(probability=True),
    "Voting Classifier": VotingClassifier(
        estimators=[("rf", RandomForestClassifier()), ("gb", GradientBoostingClassifier()), ("xgb", XGBClassifier())], voting='soft'
    ),
    "Bagging Classifier": BaggingClassifier(random_state=42),
    "Stacking Classifier": StackingClassifier(
        estimators=[("rf", RandomForestClassifier()), ("gb", GradientBoostingClassifier()), ("xgb", XGBClassifier())]
    )
}

# Train and evaluate models
results = {}
best_model = None
best_score = 0

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier, BaggingClassifier, StackingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score # Import accuracy_score and other metrics

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else y_pred

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba)

    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1,
        "ROC-AUC": roc_auc
    }

    if roc_auc > best_score:
        best_score = roc_auc
        best_model = model

    print(f"{name}: Accuracy = {accuracy:.4f}, Precision = {precision:.4f}, Recall = {recall:.4f}, F1 = {f1:.4f}, ROC-AUC = {roc_auc:.4f}")

# Convert results into a DataFrame for easy comparison
results_df = pd.DataFrame(results, columns=["Model", "MAE", "MSE", "R2 Score"])
print(results_df.sort_values(by="R2 Score", ascending=False))

# Convert results to DataFrame
results_df = pd.DataFrame(results).T
print(results_df)

# Plot results
plt.figure(figsize=(10, 5))
sns.heatmap(results_df, annot=True, cmap="coolwarm", fmt=".4f")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Models")
plt.title("Model Performance Comparison")
plt.show()

# Save the best model as a pickle file
import pickle # Import the pickle module
pickle_filename = "best_model.pkl"
with open(pickle_filename, "wb") as file:
    pickle.dump(best_model, file)

print(f"Best model saved as {pickle_filename}")

"""Use Hyperparameter tuning."""

# Define models with hyperparameter tuning
param_grid = {
    "Random Forest": {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20]
    },
    "Gradient Boost": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.1, 0.2]
    },
    "XGBR": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.1, 0.2],
        "max_depth": [3, 5, 7]
    },
    "LGBMR": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.1, 0.2]
    }
}

models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "ElasticNet": ElasticNet(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Ada Boost": AdaBoostRegressor(random_state=42),
    "Gradient Boost": GradientBoostingRegressor(random_state=42),
    "LGBMR": LGBMRegressor(random_state=42),
    "XGBR": XGBRegressor(random_state=42),
    "SVM": SVR()
}

best_model = None
best_r2 = -np.inf

for name, model in models.items():
    print(f"Training {name}...")

    if name in param_grid:
        grid_search = GridSearchCV(model, param_grid[name], cv=3, scoring='r2')
        grid_search.fit(X_train, y_train)
        model = grid_search.best_estimator_
    else:
        model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"{name} Performance:")
    print(f"Best Parameters: {grid_search.best_params_ if name in param_grid else 'Default'}")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    print("--------------------------------------------")

# Import GridSearchCV from sklearn.model_selection
from sklearn.model_selection import GridSearchCV
import joblib

for name, model in models.items():
    print(f"Training {name}...")

    if name in param_grid:
        # Now GridSearchCV is defined and accessible
        grid_search = GridSearchCV(model, param_grid[name], cv=3, scoring='r2')
        grid_search.fit(X_train, y_train)
        model = grid_search.best_estimator_
    else:
        model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"{name} Performance:")
    print(f"Best Parameters: {grid_search.best_params_ if name in param_grid else 'Default'}")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    print("--------------------------------------------")

if r2 > best_r2:
        best_r2 = r2
        best_model = model

# Save the best trained model
joblib.dump(best_model, "best_machine_failure_model1.pkl")
joblib.dump(scaler, "scaler.pkl")

# prompt: import this file to streamlit
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# Load the trained model and scaler
best_model = pickle.load(open("best_model.pkl", "rb"))
# scaler = pickle.load(open("scaler.pkl", "rb"))


# Streamlit app
st.title("Machine Failure Prediction App")

st.write("Please enter the following machine parameters:")

# Input fields for machine parameters
# Assuming you have features like 'Type', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'
type_input = st.selectbox("Type", ["L", "M", "H"])
air_temp = st.number_input("Air temperature [K]")
process_temp = st.number_input("Process temperature [K]")
rotational_speed = st.number_input("Rotational speed [rpm]")
torque = st.number_input("Torque [Nm]")
tool_wear = st.number_input("Tool wear [min]")


# Function to make prediction
def make_prediction(type_input, air_temp, process_temp, rotational_speed, torque, tool_wear):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        "Type": [type_input],
        "Air temperature [K]": [air_temp],
        "Process temperature [K]": [process_temp],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear]
    })

    # Encode categorical variable 'Type' (if applicable)
    label_encoder = LabelEncoder()
    input_data["Type"] = label_encoder.fit_transform(input_data["Type"])

    # Normalize the input data using the loaded scaler
    # input_data = scaler.transform(input_data)

    prediction = best_model.predict(input_data)
    return prediction

# Button to make prediction
if st.button("Predict Machine Failure"):
    prediction = make_prediction(type_input, air_temp, process_temp, rotational_speed, torque, tool_wear)
    if prediction == 1:
        st.error("Machine failure is predicted.")
    else:
        st.success("Machine failure is not predicted.")

import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = "best_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Title
st.title("Predictive Maintenance Model")

# Input fields
air_temp = st.number_input("Air Temperature (K)", value=300.0)
process_temp = st.number_input("Process Temperature (K)", value=310.0)
rotational_speed = st.number_input("Rotational Speed (rpm)", value=1500)
torque = st.number_input("Torque (Nm)", value=40.0)
tool_wear = st.number_input("Tool Wear (min)", value=10)

# Make Prediction
if st.button("Predict"):
    input_data = np.array([[air_temp, process_temp, rotational_speed, torque, tool_wear]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Failure' if prediction[0] == 1 else 'No Failure'}")
