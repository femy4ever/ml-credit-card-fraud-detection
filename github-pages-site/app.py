from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, PowerTransformer


app = Flask(__name__, static_url_path='/static', static_folder='static')
#data = pd.read_csv('creditCard.csv')
model = joblib.load('rfc_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        df = pd.DataFrame(data, index=[0])

        try:
            processed_data = df.astype(float)
            prediction = model.predict(processed_data)
            if prediction[0] == 1:
                predicted_class = 'Fraudulent'
            else:
                predicted_class = 'Non-Fraudulent'

            return jsonify({'prediction': predicted_class})

        except Exception as e:
            return jsonify({'error': str(e)})
        
@app.route('/instructions')
def how_it_works():
    return render_template('instructions.html')
            
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
