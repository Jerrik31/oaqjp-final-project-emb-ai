"""
Flask application for detecting emotions in a given text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route('/emotionDetector')
def detect_emotion():
    """
    API endpoint to detect emotions from input text.
    Expects a query parameter `textToAnalyze`.
    Returns a JSON response with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided! Please try again.", 400

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again!", 400

    return (f"For the given statement, the system response is anger: {response['anger']}, disgust: {response['disgust']}, fear: {response['fear']}, joy: {response['joy']} and sadness:{response['sadness']}, The dominant emotion is {response['dominant_emotion']} ",200 )


@app.route('/')
def index():
    """
    Renders the home page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
