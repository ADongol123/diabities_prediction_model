# app.py
from flask import Flask, render_template, request
import joblib  # or use torch if your model is a PyTorch model
import numpy as np

app = Flask(__name__)

# Load your model
model = joblib.load('diabetes_model.pth')  # Use torch.load if it’s a PyTorch model
model.eval()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from form
    input_features = [float(x) for x in request.form.values()]
    input_array = np.array([input_features])
    
    # Make prediction
    prediction = model.predict(input_array)
    output = 'Diabetes Detected' if prediction[0] == 1 else 'No Diabetes Detected'

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
