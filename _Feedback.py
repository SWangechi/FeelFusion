import streamlit as st

def feedback():
    st.title("📝 Your Feedback Matters")
    
    # User can enter feedback
    feedback_text = st.text_area("Please share your feedback:")
    
    # Submit button
    if st.button("Submit Feedback"):
        if feedback_text.strip():
            # Placeholder for submitting feedback logic (e.g., saving it to a database)
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter some feedback before submitting.")
    else:
        st.write("We appreciate your thoughts. Your feedback will help us improve the app.")
