import pandas as pd
import pickle
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load and fit model once
df = pd.read_csv('mtcars.csv')

# Drop the 'model' column if it exists
if 'model' in df.columns:
    df = df.drop(columns=['model'])

X = df.drop(columns=['mpg'])

y = df['mpg']
model = LinearRegression().fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

@app.route('/')
def index():
    return "Mtcars Linear Regression API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict(input_df)[0]
    return jsonify({'predicted_mpg': prediction})
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=5001)


