from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text_to_analyze = request.form["text_to_analyze"]
    result = emotion_detector(text_to_analyze)
    return render_template("index.html", result=result, text=text_to_analyze)



@app.route("/")
def render_index_page():
    return render_template("index.html")
