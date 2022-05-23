from flask import Flask, request, jsonify
from fastai.basic_train import load_learner
from fastai.vision import open_image
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

# load the learner
learn = load_learner(path='./models', file='trained_model_xlmr.pkl')
classes = learn.data.classes


def predict_single(text):
    'function to take text and return prediction'
    prediction = learn.predict(text))
    probs_list = prediction[2].numpy()
    return {
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 3) for (i, c) in enumerate(classes)}
    }


# route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    return jsonify(predict_single(request.files['text']))

if __name__ == '__main__':
    app.run()