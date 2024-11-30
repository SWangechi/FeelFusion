import streamlit as st
import os

# Set page config for title and layout
st.set_page_config(page_title="FeelFusion", page_icon="🧠", layout="wide")

# Custom CSS to apply styles
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: #333;
        font-family: 'Poppins', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #04C6C9;
        color: white;
    }
    .sidebar .sidebar-title {
        font-family: 'Poppins', sans-serif;
    }
    .sidebar .css-1v0mbdj {
        font-family: 'Poppins', sans-serif;
        font-size: 24px;
    }
    .header-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 36px;
        color: #04C6C9;
    }
    .header-subtitle {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 24px;
        color: #04C6C9;
    }
    .main-content {
        padding-top: 50px;
        text-align: center;
    }
    .main-image {
        display: block;
        margin: 0 auto;
        width: 50%; /* Adjust size as needed */
    }
    button {
        background-color: #D3615A;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px;
    }
    button:hover {
        background-color: #c84d49;
    }
    .logo-text {
        font-family: 'Poppins', sans-serif;
        font-size: 36px;
        color: #04C6C9;  /* Blue color */
        font-weight: bold;
        text-align: center;
    }
    .resources-link {
        font-size: 18px;
        color: #04C6C9;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Landing Page Section (Header and Image)
st.markdown('<h1 class="header-title">Welcome to FeelFusion</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header-subtitle">I am your virtual therapist</h2>', unsafe_allow_html=True)

# Image below the welcome text
image_path = "app/static/images/doctor_image.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)  # Display the image below the welcome text
else:
    st.text("Doctor image not found")

# # Sentiment Analysis Input (Display on Home page)
# sentiment_text = st.text_area("Share your thoughts with me:")

# if sentiment_text:
#     # Example sentiment analysis (This can be linked to a model)
#     st.text("Analyzing sentiment...")  # Placeholder for sentiment analysis result

# Sidebar - Logo as text in blue (FeelFusion)
st.sidebar.markdown('<div class="logo-text">FeelFusion</div>', unsafe_allow_html=True)

# Sidebar Navigation
menu = ["Home", "Dashboard", "Resources", "Feedback"]
choice = st.sidebar.selectbox("Menu", menu)

# Home Page: Informative Description
if choice == "Home":
    # Quick Introduction to the app
    st.markdown("""
        # Welcome to FeelFusion: Your Virtual Mental Health Companion
        
        FeelFusion is designed to support your mental well-being by providing personalized sentiment analysis, resources, and a safe space to share your feelings. 
        Whether you're feeling down, need resources, or want to track your mental health progress, FeelFusion is here for you.
        
        **Key Features**:
        - **Sentiment Analysis**: Share your thoughts, and we’ll analyze your sentiment to provide insights.
        - **Mental Health Resources**: Access helpful resources to improve your well-being.
        - **Feedback**: Share your feedback to help us improve our services.
        
        Start by sharing your thoughts, and let's take the first step together toward better mental health!
    """)

elif choice == "Dashboard":
    # Brief description of the Dashboard's functionality
    st.markdown("""
        # Dashboard: Monitor Your Mental Health Progress
        
        The Dashboard gives you an overview of your mental health journey. Here, you can:
        - View your sentiment analysis history.
        - Track changes in your mental well-being over time.
        - Access key insights based on your inputs.
        
        Take a moment to reflect on your progress and see how you're doing. Ready to dive deeper? Let's go!
    """)
    import pages._Dashboard as dashboard
    dashboard.display_dashboard()

elif choice == "Resources":
    import pages._Resources as resources
    resources.resources()  # Resources page logic to be defined

elif choice == "Feedback":
    import pages._Feedback as feedback
    feedback.feedback()  # Feedback page logic to be defined
