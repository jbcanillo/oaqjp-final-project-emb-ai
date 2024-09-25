"""
Emotion Detector Flask Application.

This module provides a web application for detecting emotions 
from text using the Emotion Detection service. It includes 
routes for analyzing text and rendering the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Analyze the text for emotions and return the results."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Show invalid text when result is none
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Initialize an empty list to collect emotion strings
    emotions = []

    # Extract the values from the response and convert everything to string
    for key, value in response.items():
        if key != "dominant_emotion":
            emotions.append(f"'{key}': {value}")

    # Join the emotions list into a single string
    emotions_str = ", ".join(emotions)

    # Return a formatted string
    return f"For the given statement, the system response is { emotions_str }. \
    The dominant emotion is { response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
