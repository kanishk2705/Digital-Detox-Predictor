# 📱 Digital Detox Predictor (AI-Powered)

### *Are you owning your phone, or is it owning you?*

---

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
