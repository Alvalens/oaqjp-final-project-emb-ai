import json
import requests


def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    obj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=obj, headers=headers)

    result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        result["anger"] = emotions["anger"]
        result["disgust"] = emotions["disgust"]
        result["fear"] = emotions["fear"]
        result["joy"] = emotions["joy"]
        result["sadness"] = emotions["sadness"]

        dominant_emotion = max(emotions, key=emotions.get)
        result["dominant_emotion"] = dominant_emotion

    return result
