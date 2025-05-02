from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    emotions_str = "anger: {}, disgust: {}, fear: {}, joy: {}, sadness: {}".format(
        result["anger"],
        result["disgust"],
        result["fear"],
        result["joy"],
        result["sadness"],
    )

    return "For the given statement, the system response is {} and the dominant emotion is {}.".format(
        emotions_str, result["dominant_emotion"]
    )


@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
