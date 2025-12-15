# Students-Social-Media-Addiction
A machine learning project that analyzes student social media usage, cleans and visualizes data, and predicts addiction scores using a Random Forest model. Includes EDA, feature engineering, and a Streamlit web app for real-time predictions.

# Project Overview:

This project analyzes students’ social media usage patterns and predicts their **Addicted Score** using Machine Learning. It includes data cleaning, exploratory data analysis (EDA), model building, and a **Streamlit web application** for real-time predictions.

## Objectives:

* Understand factors influencing social media addiction among students
* Perform data preprocessing and visualization
* Build a predictive machine learning model
* Deploy an interactive Streamlit app for addiction score predictio

## Technologies Used:

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

##  Dataset:

* **Students Social Media Addiction Dataset**
* Features include:

  * Average daily usage hours
  * Academic performance impact
  * Sleep hours per night
  * Mental health score
  * Addiction score (target variable)

## Data Processing:

* Removed duplicates and handled missing values
* Encoded categorical variables
* Scaled numerical features
* Performed correlation analysis and visualizations

##  Model:

* **Random Forest Regressor**
* Trained on cleaned and scaled data
* Evaluated using **R² Score**

##  Streamlit Web App:

The Streamlit app allows users to:

* Input student details
* Predict the **Addicted Score** instantly
* Visualize results in an interactive interface

##  How to Run the Project:

###  Install Dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

###  Run Model Training:

```bash
python colabcodeprj1.py
```

###  Launch Streamlit App:

```bash
streamlit run streamlitcodeprj1.py
```

##  Results:

* The model effectively identifies patterns related to social media addiction.
* Higher usage hours and poor mental health scores show strong correlation with addiction.

##  Future Enhancements:

* Add more ML models for comparison
* Improve UI with visual dashboards
* Deploy the app online

##  Author:

**Mary Disney A**
