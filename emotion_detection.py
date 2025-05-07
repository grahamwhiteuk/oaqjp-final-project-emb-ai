import requests
import json

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS={
    "content-type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze: str) -> dict:
    empty_response = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze:
        return empty_response

    # http request
    body = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(URL, headers=HEADERS, json=body)

    if r.status_code == 400:
        return empty_response
    
    # parse response
    response = r.json()
    output = response["emotionPredictions"][0]["emotion"]

    # find and set dominant emotion
    output["dominant_emotion"] = max(output, key=output.get)
    
    # return results
    return output

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))