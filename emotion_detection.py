import requests
import json

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS={
    "content-type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze: str) -> dict:
    # http request
    body = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(URL, headers=HEADERS, json=body)
    
    # parse response
    response = r.json()
    output = response["emotionPredictions"][0]["emotion"]

    # find and set dominant emotion
    output["dominant_emotion"] = max(output, key=output.get)
    
    # return results
    return output

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))