import streamlit as st

# import joblib
# from pathlib import Path

# model_path = Path(__file__).parent / "student_performance.joblib"
# model = joblib.load(model_path)

# 2.85789445 * 6 + 1.01771889 * 89 + -0.66491083 * 1 + 0.4810669 * 7 +  0.19533686 * 7 -33.42990290279858


m1 = 2.85789445
m2 = 1.01771889
m3 = -0.66491083
m4 = 0.4810669
m5 = 0.19533686
c  = (-33.42990290279858)



name = st.text_input(label = "Student name", placeholder = "Enter your name")

class_name = st.text_input(label = "Class name", placeholder = "Enter your class")

hour_study = st.text_input(label = "Hour study", placeholder = "Enter how many hours you studied")

previous_score = st.text_input(label = "Previous score", placeholder = "Whats your previous score ")

extra_curicular_activity = st.selectbox(label = "Extra curicular activities",options=["Yes" ,"No"], placeholder = "Anything extra you do")

sleep_hour = st.text_input(label = "Sleep hours", placeholder = "How many hours you slept")

sample_question = st.text_input(label = "Sample question paper", placeholder = "How many sample question paper you solved") 

dict =  {
    "Yes" : 1,
    "No" : 0
}

if st.button("CHECK SCORE"):
    # prediction = model.predict([[int(hour_study),int(previous_score),int(dict[extra_curicular_activity]),int(sleep_hour), int(sample_question)]])
    # st.write(f"The predicted score is {round(prediction[0])} % ")
     
    output =  m1 * int(hour_study) + m2 * int(previous_score) + m3 * int(dict[extra_curicular_activity]) + m4 * int(sleep_hour) + m5 * int(sample_question) + c

    st.write(f"The predicted score you can get could be arround {round(output)} % ")
    st.success("PERFORMANCE PREDICTED" ,icon = "✅")

#  py -m streamlit run "C:\Users\Jay Mankotia\Desktop\AI ML\03 Hours Study MLR\02_user_interface_.py" 

