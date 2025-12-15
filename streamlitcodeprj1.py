import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv(r"C:\Users\Mery\Downloads\Students Social Media Addiction (1).csv")


# Select required columns
data = data[
    [
        'Student_ID',
        'Avg_Daily_Usage_Hours',
        'Affects_Academic_Performance',
        'Sleep_Hours_Per_Night',
        'Mental_Health_Score',
        'Addicted_Score'
    ]
]

# Convert Yes/No to numeric if needed
if data['Affects_Academic_Performance'].dtype == 'object':
    data['Affects_Academic_Performance'] = data['Affects_Academic_Performance'].map(
        {'Yes': 1, 'No': 0}
    )

# -----------------------------
# Split data
# -----------------------------
X = data.drop('Addicted_Score', axis=1)
y = data['Addicted_Score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# Train model
# -----------------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📱 Student Social Media Addiction Prediction")
st.write("Enter student details to predict **Addicted Score**")

student_id = st.text_input("Student ID")
avg_usage = st.number_input("Avg Daily Usage Hours", min_value=0.0, step=0.5)
academic_affect = st.text_input("Affects Academic Performance (Yes / No)")
sleep_hours = st.number_input("Sleep Hours Per Night", min_value=0.0, step=0.5)
mental_health = st.number_input("Mental Health Score", min_value=0.0, step=1.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Addicted Score"):

    academic_value = 1 if academic_affect.lower() == "yes" else 0

    input_data = [[
        avg_usage,
        float(student_id) if student_id.isdigit() else 0,
        academic_value,
        sleep_hours,
        mental_health
    ]]

    prediction = model.predict(input_data)

    st.success(f"📊 Predicted Addicted Score: **{prediction[0]:.2f}**")
