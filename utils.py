import joblib
from transformers import BertTokenizer, TFBertForSequenceClassification
import numpy as np
import tensorflow as tf

# Load the models
try:
    tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
    lr_model = joblib.load("logistic_regression.pkl")
    bert_model = TFBertForSequenceClassification.from_pretrained("app/models/bert_model")
    bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
except Exception as e:
    raise ValueError(f"Error loading models: {e}")

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
