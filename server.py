"""
Provides a Flask server for the emotion detector
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Index Route
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Emotion Detector Route
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is <b>{result['dominant_emotion']}</b>."
