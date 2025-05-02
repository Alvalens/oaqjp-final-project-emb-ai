import json
import requests


def emotion_detection(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    obj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=obj, headers=headers)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    print(formatted_response)

