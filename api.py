from flask import Flask, request, jsonify

app = Flask(__name__)

# --------------------
# 4. API Dağıtımı
# --------------------
class ModelAPI:
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        """Veri üzerinde tahmin yapar."""
        prediction = self.model.predict(data)
        return prediction

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    processed_data = data_processing.preprocess_data(data['text'])
    prediction = model_api.predict(processed_data)
    return jsonify({"prediction": prediction})
