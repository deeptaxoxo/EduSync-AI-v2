from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore
import cv2 # type: ignore
import mediapipe as mp # type: ignore
import numpy as np

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

@app.route('/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Backend is running!"})

if __name__ == '_main_':
    app.run(debug=True)