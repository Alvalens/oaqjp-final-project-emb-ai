"""
Flask server application for emotion detection from text.
This module provides a web interface to detect emotions in text using Watson API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle requests to the emotion detector endpoint.
    Analyzes the provided text and returns the detected emotions.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Break long line into multiple parts for better readability
    emotions_str = (
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}"
    )

    # Break long line into multiple parts for better readability
    return (
        f"For the given statement, the system response is {emotions_str} "
        f"and the dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    Returns the rendered HTML template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
