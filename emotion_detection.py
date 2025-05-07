import requests

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS={
    "content-type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze: str) -> str:
    body = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(URL, headers=HEADERS, json=body)
    return r.text

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))