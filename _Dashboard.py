import streamlit as st
from utils.py import predict_sentiment  # Ensure `app` is a valid module

def display_dashboard():
    st.title("📊 Mental Health Dashboard")
    st.write("Analyze mental health sentiment")
    
    # Input text for sentiment analysis
    user_input = st.text_area("Enter text for sentiment analysis", key="dashboard_text_area")
    
    # Ensure the model type is passed, e.g., "bert" or other models you might have
    model_type = "bert"  # You can define this based on your application logic or user choice
    
    if st.button("Analyze Sentiment", key="dashboard_button"):
        sentiment = predict_sentiment(user_input, model_type)  # Provide both arguments
        st.write(f"Predicted Sentiment: {sentiment}")
    # Displaying example sentiment history (to be replaced with real data)
    st.subheader("Sentiment History")
    st.write("This is where sentiment trends will be displayed, such as mood over time.")

    # Example of a simple bar chart (replace with your actual data)
    st.bar_chart([1, 2, 3, 4, 5])  # Placeholder for the sentiment history graph

    st.write("Feel free to explore the other sections for more insights.")


# import streamlit as st
# from utils import predict_sentiment  # Import directly if `app` is in the Python path

# def dashboard():
#     st.title("📊 Mental Health Dashboard")
#     st.subheader("Analyze Sentiment from Text")
    
#     text = st.text_area("Enter text for analysis:")
#     model = st.selectbox("Choose a model:", ["Logistic Regression", "BERT"])
    
#     if st.button("Analyze"):
#         if text:
#             result = predict_sentiment(text, model.lower())
#             st.success(f"The sentiment is **{result}**.")
#         else:
#             st.error("Please enter some text.")

# dashboard()
