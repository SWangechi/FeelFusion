import os
import joblib
import gdown
from transformers import BertTokenizer, TFBertForSequenceClassification
import numpy as np
import tensorflow as tf

# Constants for model paths and Google Drive URLs
BERT_MODEL_URL = "https://drive.google.com/drive/folders/1YsVHaAorrtfGFlIXpnikaxVwMDli34Cc?usp=sharing"
BERT_MODEL_PATH = "models/bert_model"
TFIDF_PATH = "tfidf_vectorizer.pkl"
LR_MODEL_PATH = "logistic_regression.pkl"

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Function to download models from Google Drive
def download_model(url, output_path):
    if not os.path.exists(output_path):
        print(f"Downloading model from {url}...")
        gdown.download(url, output_path, quiet=False)
    else:
        print(f"Model already exists at {output_path}.")

# Load Models
try:
    # Download BERT model
    download_model(BERT_MODEL_URL, BERT_MODEL_PATH)

    # Load TF-IDF and Logistic Regression models
    if os.path.exists(TFIDF_PATH) and os.path.exists(LR_MODEL_PATH):
        tfidf_vectorizer = joblib.load(TFIDF_PATH)
        lr_model = joblib.load(LR_MODEL_PATH)
    else:
        raise FileNotFoundError("TF-IDF or Logistic Regression model files are missing.")

    # Initialize BERT Tokenizer and Model
    bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    bert_model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
    bert_model.load_weights(BERT_MODEL_PATH)

except Exception as e:
    raise RuntimeError(f"Error loading models: {e}")

# Mental health-related keywords
mental_health_keywords = {
    'Neurodevelopmental Disorders': ['autism', 'adhd', 'learning disability', 'speech delay'],
    'Schizophrenia Spectrum Disorders': ['hallucination', 'delusion', 'paranoia', 'psychotic'],
    'Bipolar Disorders': ['manic', 'hypomanic', 'mood swing', 'euphoric', 'irritable'],
    'Depressive Disorders': ['depressed', 'hopeless', 'worthless', 'sad', 'suicide', 'crying'],
    'Anxiety Disorders': ['anxious', 'panic', 'phobia', 'nervous', 'worried', 'tense'],
    'Obsessive-Compulsive Disorders': ['ocd', 'compulsive', 'obsessive', 'ritual', 'hoarding'],
    'Trauma- and Stressor-Related Disorders': ['ptsd', 'trauma', 'abuse', 'flashback', 'hypervigilance'],
    'Eating Disorders': ['anorexia', 'bulimia', 'binge eating', 'purging', 'overeating'],
    'Sleep-Wake Disorders': ['insomnia', 'nightmare', 'narcolepsy', 'sleepwalking', 'fatigue'],
    'Substance Use Disorders': ['addiction', 'withdrawal', 'alcoholic', 'drug abuse', 'dependence'],
    'Personality Disorders': ['borderline', 'antisocial', 'narcissistic', 'avoidant', 'paranoid'],
}

# Prediction function
def predict_sentiment(text, model_type):
    """
    Predicts sentiment of a given text using the selected model or based on keywords.
    
    Args:
        text (str): Input text for analysis.
        model_type (str): Model type - 'lr' (Logistic Regression) or 'bert'.
    
    Returns:
        str: Sentiment result - 'Positive' or 'Negative', or classified mental health condition.
    """
    try:
        # Check for keywords first
        for category, keywords in mental_health_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                return f"Possible condition: {category}"

        if model_type == "lr":
            # TF-IDF + Logistic Regression
            features = tfidf_vectorizer.transform([text])
            prediction = lr_model.predict(features)[0]
            return "Positive" if prediction == 1 else "Negative"

        elif model_type == "bert":
            # Preprocess input for BERT
            tokens = bert_tokenizer(text, return_tensors="tf", truncation=True, padding=True, max_length=128)
            logits = bert_model(tokens).logits
            sentiment = tf.argmax(logits, axis=1).numpy()[0]
            return "Positive" if sentiment == 1 else "Negative"

        else:
            return "Invalid model type. Please choose 'lr' or 'bert'."

    except Exception as e:
        raise ValueError(f"Error in prediction: {e}")
