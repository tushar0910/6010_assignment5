from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("news_category_classifier")
vectorizer = joblib.load("vectorizer.pkl")

# Define /classify endpoint
@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    if not data or "headline" not in data:
        return jsonify({"error": "Missing 'headline' in request"}), 400

    headline = data["headline"]
    X = vectorizer.transform([headline])
    prediction = model.predict(X)[0]

    return jsonify({"category": prediction})

# Optional: Root route for health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "News Classifier API is running"}), 200
