"""
Emotion Detection Module.
This module provides functions to analyze text for emotional content using a Watson API.
"""

import json
import re
import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the provided text.

    Args:
        text_to_analyze (str): The text to analyze for emotional content.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              If the text is invalid or the analysis fails, all values will be None.
    """
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    obj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not text_to_analyze or text_to_analyze.strip() == "":
        return result

    response = requests.post(URL, json=obj, headers=headers)

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

    elif response.status_code == 400:
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return result
