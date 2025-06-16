from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

# Dummy training data
X = ["free offer", "hello friend", "win money", "meeting schedule", "cheap meds"]
y = [1, 0, 1, 0, 1]

# Create pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train model
model.fit(X, y)

# Ensure model directory exists
os.makedirs('model', exist_ok=True)

# Save the model
joblib.dump(model, 'model/spam_model.pkl')
print("✅ Model saved to model/spam_model.pkl")
