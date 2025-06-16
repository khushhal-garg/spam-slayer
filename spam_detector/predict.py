import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'spam_model.pkl')
model = joblib.load(model_path)

def predict_spam(message):
    prediction = model.predict([message])
    return bool(prediction[0])
