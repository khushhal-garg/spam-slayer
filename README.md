# Spam Slayer

**Spam Slayer** is a high-performance, modular spam detection API powered by machine learning. Developed using **Python (Flask)**, it offers seamless integration with backend frameworks such as **Spring Boot**, providing real-time predictions on whether a message is spam.

---

## Features

- ML-based text classification using Naive Bayes  
- RESTful API built with Flask  
- Cross-platform compatibility – easily callable from any backend (Java, Node.js, etc.)  
- Pre-trained model included with support for retraining  

---

## Tech Stack

- Python 3.x  
- Flask  
- scikit-learn  
- joblib  

---

## Example Request and Response

### Request
```json
POST /detect-spam
{
  "message": "Congratulations! You've won a free iPhone!"
}

### Response
{
  "spam": true
}


