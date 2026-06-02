# 🏏 IPL Score Predictor

An AI-powered IPL First Innings Score Prediction System built using Machine Learning and Streamlit. The application predicts the final innings score based on the current match situation, venue conditions, team combinations, and recent match momentum.

---

## 📌 Project Overview

IPL matches are highly dynamic, and predicting the final score during an innings is a challenging machine learning problem. This project leverages historical IPL ball-by-ball data and a CatBoost Regression model to estimate the final innings total with high accuracy.

The application provides an interactive IPL-themed dashboard where users can select teams, venue, and current match conditions to obtain a real-time score prediction.

---

## 🚀 Live Features

### Match Prediction

* Predicts final first-innings score.
* Generates score range estimates.
* Calculates projected run rate.
* Provides prediction confidence indicators.

### Team Insights

* Captain information.
* Star player information.
* IPL title count.
* Franchise-specific dashboard cards.

### Venue Insights

* Stadium information.
* Pitch behavior.
* Historical facts.
* IPL final-related information.

### Input Validation

* Prevents impossible match situations.
* Validates runs and wickets in the last 5 overs.
* Ensures cricket score logic consistency.

### Interactive Dashboard

* IPL-inspired UI.
* Dark premium theme.
* Responsive design.
* Real-time prediction updates.

---

## 🧠 Machine Learning Pipeline

### Dataset

The model was trained on historical IPL ball-by-ball data containing:

* Venue
* Batting Team
* Bowling Team
* Current Runs
* Wickets Lost
* Overs Completed
* Runs Scored in Last 5 Overs
* Wickets Lost in Last 5 Overs
* Final Innings Total

### Dataset Statistics

* Total Records: 76,014+
* Match Type: IPL T20
* Training Data: Historical IPL innings data

---

## 📊 Feature Selection

The following features were selected after exploratory data analysis and correlation analysis:

| Feature        | Description                   |
| -------------- | ----------------------------- |
| venue          | Stadium where match is played |
| bat_team       | Current batting team          |
| bowl_team      | Current bowling team          |
| runs           | Current score                 |
| wickets        | Current wickets lost          |
| overs          | Overs completed               |
| runs_last_5    | Runs scored in last 5 overs   |
| wickets_last_5 | Wickets lost in last 5 overs  |

Target Variable:

```text
total
```

Final innings score.

---

## 🤖 Model Used

### CatBoost Regressor

CatBoost was selected because:

* Handles categorical features effectively.
* Requires minimal preprocessing.
* Performs exceptionally well on tabular data.
* Reduces overfitting.
* Provides strong predictive accuracy.

Model Configuration:

```python
CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    loss_function='RMSE',
    random_state=42
)
```

---

## 📈 Model Performance

### Evaluation Metrics

| Metric   | Score |
| -------- | ----- |
| MAE      | 6.68  |
| RMSE     | 9.59  |
| R² Score | 0.89  |

### Interpretation

* Average prediction error is approximately 6–7 runs.
* Predictions generally remain within ±10 runs of actual scores.
* Model explains approximately 89% of score variance.

These results indicate strong predictive performance for a live cricket score prediction system.

---

## 🏗️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* CatBoost

### Frontend

* Streamlit
* Custom CSS
* Responsive Dashboard Design

### Model Persistence

* Joblib

---

## 📂 Project Structure

```text
IPL_SCORE_PRED/

│
├── app.py
├── ipl_score_predictor.pkl
├── teams.pkl
├── venues.pkl
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── catboost_info/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd IPL_SCORE_PRED
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Application Workflow

1. Select Batting Team.
2. Select Bowling Team.
3. Choose Match Venue.
4. Enter:

   * Current Runs
   * Wickets Lost
   * Overs Completed
   * Runs in Last 5 Overs
   * Wickets in Last 5 Overs
5. Click Predict Final Score.
6. View:

   * Predicted Score
   * Score Range
   * Projected Run Rate
   * Team Insights
   * Venue Insights

---

## 🔍 Future Improvements

Potential enhancements include:

* Live IPL API integration.
* Real-time score updates.
* Win probability prediction.
* Match outcome prediction.
* Player-level analytics.
* Team strength ratings.
* Advanced visualizations.
* Historical venue statistics.
* Player impact scores.

---

## 💡 Key Learnings

Through this project, the following concepts were explored:

* Exploratory Data Analysis (EDA)
* Feature Engineering
* Regression Modeling
* CatBoost Implementation
* Model Evaluation
* Model Serialization
* Streamlit Development
* UI/UX Design for ML Applications
* End-to-End Machine Learning Deployment

---

## 📜 License

This project is developed for educational and portfolio purposes.

---

## 👨‍💻 Author

Shubham Kumar

B.Tech Electronics and Communication Engineering
Birla Institute of Technology Mesra

GitHub: https://github.com/shubham-kumar145

LinkedIn: https://www.linkedin.com/in/shubham-kumar145/

Portfolio: https://shubhamkumar.me
