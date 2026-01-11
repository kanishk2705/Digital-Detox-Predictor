import streamlit as st
import pandas as pd
import joblib
st.set_page_config(page_title="Digital Detox Predictor",layout="centered")
MODEL_COLUMNS = [
    'Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 'Mental_Health_Score', 
    'Conflicts_Over_Social_Media', 'Gender_Male', 'Academic_Level_High School', 
    'Academic_Level_Undergraduate', 'Most_Used_Platform_Instagram', 
    'Most_Used_Platform_KakaoTalk', 'Most_Used_Platform_LINE', 
    'Most_Used_Platform_LinkedIn', 'Most_Used_Platform_Snapchat', 
    'Most_Used_Platform_TikTok', 'Most_Used_Platform_Twitter', 
    'Most_Used_Platform_VKontakte', 'Most_Used_Platform_WeChat', 
    'Most_Used_Platform_WhatsApp', 'Most_Used_Platform_YouTube', 
    'Affects_Academic_Performance_Yes', 'Relationship_Status_In Relationship', 
    'Relationship_Status_Single'
]
@st.cache_resource
def load_model_objects():
    model = joblib.load("addiction_predictor_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model,scaler

try:
    model, scaler = load_model_objects()
except FileNotFoundError:
    st.error("⚠️ Error: Model files not found. Please make sure 'addiction_predictor_model.pkl' and 'scaler.pkl' are in the same folder.")
    st.stop()

# User Interface
st.title("📱 Digital Detox AI")
st.markdown("### Are your digital habits healthy? Let's Check!")

st.sidebar.header("User Profile")

age = st.sidebar.number_input("Age",min_value=10,max_value=80,value=20)
gender = st.sidebar.selectbox("Gender",["Male", "Female"])
academic_status = st.sidebar.selectbox("Academic Level",["School","Undergraduate","Postgraduate"])

st.sidebar.header("Digital Habits")

usage_hours = st.sidebar.slider("Daily Screen Time(Hours)",0,24,5)
sleep_hours = st.sidebar.slider("Sleep Per Night(Hours)",0,12,7)
platform = st.sidebar.selectbox("Most Used App", [
    "Instagram", "TikTok", "YouTube", "WhatsApp", "Twitter", "Snapchat", 
    "LinkedIn", "WeChat", "LINE", "KakaoTalk", "VKontakte", "Other"
])
conflicts = st.sidebar.slider("Conflicts over Family for phone (Scale 0 to 5)",0,5,0)

st.sidebar.header("Well Being")

mental_health = st.sidebar.slider("Self Reported Mental Health (1 = Poor, 10 = Excellent)",1,10,7)
academic_impact = st.sidebar.radio("Does phone use affect your grades?",["No","Yes"])
relationship = st.sidebar.selectbox("Relationship Status", ["Single", "In Relationship", "Married/Divorced/Other"])

if st.button("Analyze Risk"):
    
    # A. Initialize a dictionary with all columns set to 0
    input_data = {col: 0 for col in MODEL_COLUMNS}
    
    # B. Fill in the Numerical Values (Direct Mapping)
    input_data['Age'] = age
    input_data['Avg_Daily_Usage_Hours'] = usage_hours
    input_data['Sleep_Hours_Per_Night'] = sleep_hours
    input_data['Mental_Health_Score'] = mental_health
    input_data['Conflicts_Over_Social_Media'] = conflicts
    
    # C. Handle Categorical Logic (One-Hot Encoding)
    
    # Gender (If Male -> 1, If Female -> 0 (Default))
    if gender == 'Male':
        input_data['Gender_Male'] = 1
        
    # Academic Level
    if academic_status == 'High School': # Assuming "School" maps to High School
        input_data['Academic_Level_High School'] = 1
    elif academic_status == 'Undergraduate':
        input_data['Academic_Level_Undergraduate'] = 1
    # Note: 'Postgraduate' is the reference category (all 0)
        
    # Platform
    # We construct the key name dynamically. e.g. "Most_Used_Platform_TikTok"
    platform_key = f"Most_Used_Platform_{platform}"
    if platform_key in input_data:
        input_data[platform_key] = 1
        
    # Academic Impact
    if academic_impact == 'Yes':
        input_data['Affects_Academic_Performance_Yes'] = 1
        
    # Relationship
    if relationship == 'In Relationship':
        input_data['Relationship_Status_In Relationship'] = 1
    elif relationship == 'Single':
        input_data['Relationship_Status_Single'] = 1
        
    # D. Create DataFrame
    df_input = pd.DataFrame([input_data])
    
    # E. Scale the Numerical Columns (CRITICAL STEP)
    # The scaler expects specific columns to be scaled. 
    # We must ensure we scale ONLY the ones we scaled during training.
    numeric_cols = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 
                    'Mental_Health_Score', 'Conflicts_Over_Social_Media']
    
    df_input[numeric_cols] = scaler.transform(df_input[numeric_cols])

    # ------------------------------------------------------------------------------
    # 5. PREDICTION & DISPLAY
    # ------------------------------------------------------------------------------
    prediction = model.predict(df_input)[0]
    
    # Formatting the output nicely
    st.divider()
    st.subheader("Analysis Result")
    
    # Create a nice score gauge
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Predicted Addiction Score", value=f"{prediction:.2f} / 10.0")
    
    with col2:
        if prediction < 5:
            st.success("✅ Low Risk: You have a healthy digital balance.")
        elif prediction < 7:
            st.warning("⚠️ Moderate Risk: Keep an eye on your usage.")
        else:
            st.error("🚨 High Risk: Consider a Digital Detox immediately.")
            
    # Recommendations based on logic
    st.write("### 💡 AI Recommendation:")
    if usage_hours > 6:
        st.write("- Try reducing screen time by 30 mins/day.")
    if sleep_hours < 7:
        st.write("- Your sleep is low. No screens 1 hour before bed.")
    if conflicts > 2:
        st.write("- Phone usage is causing real-life arguments. Prioritize offline conversations.")