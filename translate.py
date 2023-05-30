import requests
import cfg

IAM_TOKEN = cfg.YandexAPI
folder_id = cfg.YaFolder_id

def translate(texts,target_language):
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        json = body,
        headers = headers
    )
    return response.json()['translations'][0]['text']

