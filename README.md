# 📱 Digital Detox Predictor (AI-Powered)

### *Are you owning your phone, or is it owning you?*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://digital-detox-predictor-ti4ofe4krykbecwwsgny6w.streamlit.app/)

**🚀 Live Demo:** [Click Here to Launch App](https://digital-detox-predictor-ti4ofe4krykbecwwsgny6w.streamlit.app/)  
**📊 Dashboard:** [View Power BI Analytics](#-project-structure) *(Coming Soon)*

## 📖 Project Overview
In an era of hyper-connectivity, digital addiction is a silent crisis affecting mental health, academic performance, and social relationships. 

The **Digital Detox Predictor** is an End-to-End Machine Learning application designed to:
1.  **Analyze** an individual's digital habits.
2.  **Predict** their "Addiction Risk Score" using advanced ensemble models.
3.  **Provide** actionable, personalized recommendations for a healthier digital lifestyle.

---

## 🛠️ The Development Journey
This project was built iteratively, mimicking a real-world Agile development lifecycle.

###  Phase 1: Data Engineering & Analysis 
* **Goal:** Understand the "DNA" of digital addiction.
* **Actions:**
    * Cleaned raw data (handled missing values, outliers).
    * Engineered features: Converted categorical inputs (Platform, Gender) into numerical vectors using One-Hot Encoding.
    * **Key Insight:** Found a strong correlation between *Sleep Hours* and *Addiction Score*, but surprisingly, *Message-based apps* (like WhatsApp) showed lower addiction risks than *Scroll-based apps* (like TikTok).

### Phase 2: Model Training (The Champion-Challenger Strategy)
I tested three algorithms to find the most accurate predictor.
### Model Performance Comparison

| Model | R² Score (Accuracy) | Verdict |
| :--- | :--- | :--- |
| **Linear Regression** | 97.00% | Good baseline, but struggles with non-linear patterns. |
| **Decision Tree** | 96.64% | Good logic, but prone to overfitting. |
| **Random Forest** | **97.99%** | **🏆 The Champion Model.** Stabilized variance using 100 decision trees. |
* **Outcome:** The **Random Forest Regressor** was saved (`.pkl`) as the production engine.

### Phase 3: Product Development (Streamlit)
* **Goal:** Turn the math model into a user-friendly product.
* **Tech Stack:** Python, Streamlit.
* **Features:**
    * Built a "Translation Layer" to map simple user inputs (Age, Usage) to the complex 22-feature vector expected by the model.
    * Real-time inference engine.
    * Dynamic UI with risk-level alerts (Low, Moderate, High).

### Phase 4: Deployment (DevOps)
* **Goal:** Make the app accessible globally.
* **Action:** Deployed the application on **Streamlit Community Cloud**, ensuring 24/7 availability.

---

## 💻 How to Run This Project Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/kanishk2705/Digital-Detox-Predictor.git](https://github.com/kanishk2705/Digital-Detox-Predictor.git)
   cd Digital-Detox-Predictor

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the App**
   ```bash
   streamlit run app.py

## 📂 Project Structure
The repository is organized as follows:

```text
├── 📁 data                   # Raw and Cleaned CSV files
├── 📁 notebooks              # Jupyter Notebooks (EDA & Model Training)
├── 📄 app.py                 # Main Streamlit Application
├── 📄 addiction_predictor_model.pkl    # Trained Random Forest Model
├── 📄 scaler.pkl             # Scaler object for preprocessing
├── 📄 requirements.txt       # Dependencies for cloud deployment
└── 📄 README.md              # Project Documentation

👨‍💻 Author
A C KANISHK | Aspiring Data Scientist | ML Enthusiast | https://www.linkedin.com/in/kanishk27 |
